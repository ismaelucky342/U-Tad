import cv2, numpy as np, pandas as pd, time
from pathlib import Path
ENT=Path('U1_Practica_Hernandez_Ismael'); DATA=ENT/'data'
imagenes=sorted(DATA.glob('IMG_*.jpg'))

def luminancia(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)[...,0]

def diagnostico(img):
    Y=luminancia(img).astype(np.uint8)
    hist=np.bincount(Y.ravel(),minlength=256).astype(np.float64)
    p=hist/hist.sum(); p=p[p>0]
    return {'sat_bajo':100.0*float(np.mean(Y<=2)),'sat_alto':100.0*float(np.mean(Y>=253)),
            'rango_p1_p99':float(np.percentile(Y,99)-np.percentile(Y,1)),
            'entropia':float(-(p*np.log2(p)).sum()),'desv_tipica':float(np.std(Y))}

def diagnostico_color(img):
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB).astype(np.float64)
    return {'R':float(rgb[...,0].mean()),'G':float(rgb[...,1].mean()),'B':float(rgb[...,2].mean())}

def reconstruir(img,Y2):
    ycc=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    ycc[...,0]=Y2
    return cv2.cvtColor(ycc,cv2.COLOR_YCrCb2BGR)

def aplicar_gamma(img,g):
    y=luminancia(img)
    lut=np.array([int(round(255.0*(i/255.0)**g)) for i in range(256)],dtype=np.uint8)
    return reconstruir(img,cv2.LUT(y,lut))

def estirar(img,plo,phi):
    y=luminancia(img)
    lo=float(np.percentile(y,plo)); hi=float(np.percentile(y,phi))
    if hi<=lo: return img.copy()
    y2=np.clip((y.astype(np.float64)-lo)/(hi-lo),0,1)
    return reconstruir(img,np.round(y2*255).astype(np.uint8))

def ecualizar(img):
    return reconstruir(img,cv2.equalizeHist(luminancia(img)))

def clahe(img,clip,tile):
    c=cv2.createCLAHE(clipLimit=float(clip),tileGridSize=(int(tile),int(tile)))
    return reconstruir(img,c.apply(luminancia(img)))

CONFIGS=[]
for g in [0.45,0.6,0.8,1.0,1.4,1.8,2.2]: CONFIGS.append(('gamma',f'g={g}',('gamma',g)))
for plo,phi in [(0,100),(1,99),(2,98),(5,95)]: CONFIGS.append(('estiramiento',f'p={plo}-{phi}',('est',plo,phi)))
CONFIGS.append(('he','-',('he',)))
for clip in [1.0,2.0,4.0]:
    for tile in [4,8,16]: CONFIGS.append(('clahe',f'clip={clip:.1f};tile={tile}x{tile}',('clahe',clip,tile)))
CONFIGS.append(('original','-',('orig',)))

def aplicar(img,cfg):
    op,par,args=cfg
    if op=='gamma': return aplicar_gamma(img,args[1])
    if op=='estiramiento': return estirar(img,args[1],args[2])
    if op=='he': return ecualizar(img)
    if op=='clahe': return clahe(img,args[1],args[2])
    return img.copy()

filas=[]; t0=time.time()
for p in imagenes:
    img=cv2.imread(str(p))
    for k,cfg in enumerate(CONFIGS):
        out=aplicar(img,cfg); d=diagnostico(out); c=diagnostico_color(out)
        filas.append({'imagen':p.name,'operacion':cfg[0],'parametros':cfg[1],'orden':k,**d,**c})
    print(p.name, f'{time.time()-t0:.1f}s')
df=pd.DataFrame(filas)
df.to_csv('_trabajo/prototipo_resultados.csv',index=False)

def elegir(df,img):
    sub=df[df.imagen==img]; proc=sub[sub.operacion!='original']
    ok=proc[(proc.sat_bajo<=1)&(proc.sat_alto<=1)]
    if len(ok):
        ok=ok.sort_values(['rango_p1_p99','entropia','orden'],ascending=[False,False,True])
        regla='normal'
    else:
        proc=proc.copy(); proc['peor']=np.maximum(proc.sat_bajo,proc.sat_alto)
        ok=proc.sort_values(['peor','rango_p1_p99','entropia','orden'],ascending=[True,False,False,True])
        regla='respaldo'
    return ok.iloc[0],sub[sub.operacion=='original'].iloc[0],regla,len(ok)
print('\nGANADORAS')
for p in imagenes:
    w,o,r,n=elegir(df,p.name)
    print(f"{p.name} [{r}, {n} elegibles] -> {w.operacion} {w.parametros} | rango {o.rango_p1_p99:.0f}->{w.rango_p1_p99:.0f} satb {o.sat_bajo:.2f}->{w.sat_bajo:.2f} sata {o.sat_alto:.2f}->{w.sat_alto:.2f} H {o.entropia:.2f}->{w.entropia:.2f}")
print('\nLOTE')
proc=df[df.operacion!='original'].copy()
filas=[]
for (op,par),g in proc.groupby(['operacion','parametros']):
    cumple=int((((g.sat_bajo<=1)&(g.sat_alto<=1))).sum())
    filas.append({'operacion':op,'parametros':par,'cumple':cumple,'rango_medio':g.rango_p1_p99.mean(),'entropia_media':g.entropia.mean(),'orden':int(g.orden.iloc[0])})
lote=pd.DataFrame(filas).sort_values(['cumple','rango_medio','entropia_media','orden'],ascending=[False,False,False,True])
print(lote.head(12).to_string(index=False))
