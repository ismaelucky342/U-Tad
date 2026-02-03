# 🎓 Modelos de Práctica para Examen de Sistemas Distribuidos

Este directorio contiene **4 variaciones completas** del sistema RPC original (Persona), diseñadas para que practiques para el examen. Cada variación mantiene la **misma estructura y mecánica** pero con clases y atributos diferentes.

---

## 📚 **VARIACIÓN 1: Clase Libro**

### Archivos:
- `libro.h` - Definición de la clase
- `libroRemoto.cpp` - Implementación del cliente (métodos remotos)
- `gestorClientes.h` - Header del gestor
- `gestorClientes.cpp` - Implementación del servidor (switch cases)

### Atributos:
- `string titulo`
- `string autor`
- `int numPaginas`

### Métodos Principales:
```cpp
void setTitulo(string titulo);
string getTitulo();
void setAutor(string autor);
string getAutor();
void setNumPaginas(int numPaginas);
int getNumPaginas();
void escribirAFichero(string nombreFichero);
void leerDeFichero(string nombreFichero);
```

### Enum de Mensajes:
```cpp
typedef enum{
    LibroFD, LibroFP, LibroFDe,
    setTituloF, setAutorF, setNumPaginasF,
    getTituloF, getAutorF, getNumPaginasF,
    ostreamOpF, escribirAFicheroF, leerDeFicheroF,
    ackMSG
} libroMSGTypes;
```

---

## 💰 **VARIACIÓN 2: Clase CuentaBancaria**

### Archivos:
- `cuentaBancaria.h`
- `cuentaBancariaRemota.cpp`
- `gestorClientes.h`
- `gestorClientes.cpp`

### Atributos:
- `string titular`
- `double saldo`
- `string numeroCuenta`

### Métodos Principales:
```cpp
void setTitular(string titular);
string getTitular();
void setSaldo(double saldo);
double getSaldo();
void setNumeroCuenta(string numeroCuenta);
string getNumeroCuenta();
void escribirAFichero(string nombreFichero);
void leerDeFichero(string nombreFichero);
```

### Enum de Mensajes:
```cpp
typedef enum{
    CuentaBancariaFD, CuentaBancariaFP, CuentaBancariaFDe,
    setTitularF, setSaldoF, setNumeroCuentaF,
    getTitularF, getSaldoF, getNumeroCuentaF,
    ostreamOpF, escribirAFicheroF, leerDeFicheroF,
    ackMSG
} cuentaBancariaMSGTypes;
```

**⚠️ NOTA:** Esta variación usa `double` en lugar de `int`, perfecto para practicar serialización de tipos flotantes.

---

## 🚗 **VARIACIÓN 3: Clase Vehiculo**

### Archivos:
- `vehiculo.h`
- `vehiculoRemoto.cpp`
- `gestorClientes.h`
- `gestorClientes.cpp`

### Atributos:
- `string marca`
- `string modelo`
- `int anio`
- `int kilometraje`

### Métodos Principales:
```cpp
void setMarca(string marca);
string getMarca();
void setModelo(string modelo);
string getModelo();
void setAnio(int anio);
int getAnio();
void setKilometraje(int kilometraje);
int getKilometraje();
void escribirAFichero(string nombreFichero);
void leerDeFichero(string nombreFichero);
```

### Enum de Mensajes:
```cpp
typedef enum{
    VehiculoFD, VehiculoFP, VehiculoFDe,
    setMarcaF, setModeloF, setAnioF, setKilometrajeF,
    getMarcaF, getModeloF, getAnioF, getKilometrajeF,
    ostreamOpF, escribirAFicheroF, leerDeFicheroF,
    ackMSG
} vehiculoMSGTypes;
```

**⚠️ NOTA:** Esta variación tiene **4 atributos** (2 strings y 2 ints), ideal para practicar serialización múltiple.

---

## 🛒 **VARIACIÓN 4: Clase Producto**

### Archivos:
- `producto.h`
- `productoRemoto.cpp`
- `gestorClientes.h`
- `gestorClientes.cpp`

### Atributos:
- `string nombre`
- `double precio`
- `int stock`
- `string categoria`

### Métodos Principales:
```cpp
void setNombre(string nombre);
string getNombre();
void setPrecio(double precio);
double getPrecio();
void setStock(int stock);
int getStock();
void setCategoria(string categoria);
string getCategoria();
void escribirAFichero(string nombreFichero);
void leerDeFichero(string nombreFichero);
```

### Enum de Mensajes:
```cpp
typedef enum{
    ProductoFD, ProductoFP, ProductoFDe,
    setNombreF, setPrecioF, setStockF, setCategoriaF,
    getNombreF, getPrecioF, getStockF, getCategoriaF,
    ostreamOpF, escribirAFicheroF, leerDeFicheroF,
    ackMSG
} productoMSGTypes;
```

**⚠️ NOTA:** Combina `string`, `double` e `int` - perfecta para practicar tipos mixtos.

---

## 📝 **ESTRUCTURA DEL EXAMEN**

### **PARTE 1: Cliente Remoto (XxxRemoto.cpp)**
Te pedirán implementar **UNO** de estos métodos:

#### **Ejemplo: Método GET con tipo simple (int/double)**
```cpp
int Libro::getNumPaginas(){
    int resultado=0;
    auto conn=GestorClientes::connections[this];
    vector<unsigned char> buffer;
    pack(buffer,getNumPaginasF);
    sendMSG(conn.serverId, buffer);
    buffer.clear();
    recvMSG(conn.serverId,buffer);
    
    if(buffer.size()==0){
        cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
    }
    else{    
        libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
        if(ack!=ackMSG)
            cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
        else{
            resultado=unpack<int>(buffer);
        }
    }    
    return resultado;    
}
```

#### **Ejemplo: Método GET con string**
```cpp
string Libro::getTitulo(){
    string resultado="";
    auto conn=GestorClientes::connections[this];
    vector<unsigned char> buffer;
    pack(buffer,getTituloF);
    sendMSG(conn.serverId, buffer);
    buffer.clear();
    recvMSG(conn.serverId,buffer);
    
    if(buffer.size()==0){
        cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
    }
    else{    
        libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
        if(ack!=ackMSG)
            cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
        else{
            resultado.resize(unpack<int>(buffer));
            unpackv<char>(buffer,(char*)resultado.data(),resultado.size());
        }
    }    
    return resultado;
}
```

#### **Ejemplo: Método SET con tipo simple**
```cpp
void Libro::setNumPaginas(int numPaginas){
    auto conn=GestorClientes::connections[this];
    vector<unsigned char> buffer;
    pack(buffer,setNumPaginasF);
    pack(buffer,numPaginas);
    sendMSG(conn.serverId, buffer);
    buffer.clear();
    recvMSG(conn.serverId,buffer);
    
    if(buffer.size()==0){
        cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
    }
    else{    
        libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
        if(ack!=ackMSG)
            cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
    }    
}
```

#### **Ejemplo: Método SET con string**
```cpp
void Libro::setTitulo(string titulo){
    auto conn=GestorClientes::connections[this];
    vector<unsigned char> buffer;
    pack(buffer,setTituloF);
    pack(buffer,(int)titulo.size());
    packv(buffer,(char*)titulo.data(),(int)titulo.size());
    sendMSG(conn.serverId, buffer);
    buffer.clear();
    recvMSG(conn.serverId,buffer);
    
    if(buffer.size()==0){
        cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tamaño de mensaje inválido"<<endl;
    }
    else{    
        libroMSGTypes ack=unpack<libroMSGTypes>(buffer);
        if(ack!=ackMSG)
            cout<<"ERROR: "<<__FILE__<<":"<<__LINE__<<"Tipo de mensaje inválido"<<endl;
    }    
}
```

---

### **PARTE 2: Servidor (gestorClientes.cpp)**
Te pedirán implementar **UN CASE** del switch. Ejemplos:

#### **Ejemplo: Case GET con tipo simple**
```cpp
case getNumPaginasF:{
    int numPaginas=clients[clientId].getNumPaginas();
    buffer.clear();
    pack(buffer,ackMSG);
    pack(buffer,numPaginas);
}break;
```

#### **Ejemplo: Case GET con string**
```cpp
case getTituloF:{
    string titulo=clients[clientId].getTitulo();
    buffer.clear();
    pack(buffer,ackMSG);
    pack(buffer,(int)titulo.size());
    packv(buffer,(char*)titulo.data(),(int)titulo.size());
}break;
```

#### **Ejemplo: Case SET con tipo simple**
```cpp
case setNumPaginasF:{
    int numPaginas;
    numPaginas=unpack<int>(buffer);
    clients[clientId].setNumPaginas(numPaginas);
    buffer.clear();
    pack(buffer,ackMSG);
}break;
```

#### **Ejemplo: Case SET con string**
```cpp
case setTituloF:{
    string titulo;
    titulo.resize(unpack<int>(buffer));
    unpackv<char>(buffer,(char*)titulo.data(),(int)titulo.size());
    clients[clientId].setTitulo(titulo);
    buffer.clear();
    pack(buffer,ackMSG);
}break;
```

---

## 🎯 **TIPS PARA EL EXAMEN**

### ✅ **PARTE 1 - Cliente (XxxRemoto.cpp)**
1. **Siempre** obtén la conexión: `auto conn=GestorClientes::connections[this];`
2. **Siempre** crea el buffer: `vector<unsigned char> buffer;`
3. **Empaqueta** el tipo de mensaje primero: `pack(buffer, tipoMensajeF);`
4. Para **SET**: empaqueta el parámetro después del tipo
5. Para **GET**: NO empaquetes parámetros, solo el tipo
6. **Envía** el mensaje: `sendMSG(conn.serverId, buffer);`
7. **Limpia y recibe**: `buffer.clear(); recvMSG(conn.serverId,buffer);`
8. **Valida** el ACK
9. Para **GET**: desempaqueta el resultado
10. Para **SET**: no necesitas desempaquetar nada más

### ✅ **PARTE 2 - Servidor (gestorClientes.cpp)**
1. Para **SET**: desempaqueta primero el parámetro del buffer
2. Llama al método local: `clients[clientId].metodo(parametro);`
3. Para **GET**: llama al método y guarda resultado en variable temporal
4. **Siempre**: `buffer.clear();` antes de responder
5. **Siempre**: `pack(buffer,ackMSG);` primero
6. Para **GET**: empaqueta el resultado después del ACK
7. **No olvides** el `break;` al final

### 📦 **Serialización de Strings**
```cpp
// EMPAQUETAR:
pack(buffer, (int)miString.size());
packv(buffer, (char*)miString.data(), (int)miString.size());

// DESEMPAQUETAR:
miString.resize(unpack<int>(buffer));
unpackv<char>(buffer, (char*)miString.data(), miString.size());
```

### 📦 **Serialización de Tipos Simples**
```cpp
// EMPAQUETAR:
pack(buffer, miInt);        // int
pack(buffer, miDouble);     // double

// DESEMPAQUETAR:
int valor = unpack<int>(buffer);
double valor = unpack<double>(buffer);
```

---

## 🔥 **PRACTICA ESTOS CASOS**

Para dominar el examen, practica escribir a mano (sin copiar):

### Cliente (XxxRemoto.cpp):
- [ ] `getTitulo()` - GET de string
- [ ] `getNumPaginas()` - GET de int
- [ ] `getSaldo()` - GET de double
- [ ] `setAutor(string)` - SET de string
- [ ] `setAnio(int)` - SET de int
- [ ] `setPrecio(double)` - SET de double

### Servidor (gestorClientes.cpp):
- [ ] `case getTituloF:` - GET string
- [ ] `case getNumPaginasF:` - GET int
- [ ] `case getSaldoF:` - GET double
- [ ] `case setAutorF:` - SET string
- [ ] `case setAnioF:` - SET int
- [ ] `case setPrecioF:` - SET double

---

## ⚠️ **ERRORES COMUNES A EVITAR**

1. ❌ Olvidar `buffer.clear()` antes de reutilizar el buffer
2. ❌ No validar el tamaño del buffer recibido
3. ❌ No validar el ACK
4. ❌ Olvidar el `(int)` al hacer cast del tamaño del string
5. ❌ Confundir el orden: siempre **ACK primero**, luego datos
6. ❌ En GET: intentar desempaquetar antes de validar ACK
7. ❌ En el servidor: olvidar llamar al método `clients[clientId].metodo()`
8. ❌ Olvidar el `break;` al final del case

---

## 🎓 **EJERCICIO RECOMENDADO**

1. **Imprime** estas 4 variaciones
2. **Tapa** los archivos `XxxRemoto.cpp` y `gestorClientes.cpp`
3. **Reescríbelos** a mano solo con los `.h` como referencia
4. **Compara** con los originales
5. **Repite** hasta que puedas hacerlo sin errores

---

## 📂 **ESTRUCTURA DE DIRECTORIOS**

```
2.ModelosExamen/
├── README.md (este archivo)
├── Variacion_1_Libro/
│   ├── libro.h
│   ├── libroRemoto.cpp
│   ├── gestorClientes.h
│   └── gestorClientes.cpp
├── Variacion_2_CuentaBancaria/
│   ├── cuentaBancaria.h
│   ├── cuentaBancariaRemota.cpp
│   ├── gestorClientes.h
│   └── gestorClientes.cpp
├── Variacion_3_Vehiculo/
│   ├── vehiculo.h
│   ├── vehiculoRemoto.cpp
│   ├── gestorClientes.h
│   └── gestorClientes.cpp
└── Variacion_4_Producto/
    ├── producto.h
    ├── productoRemoto.cpp
    ├── gestorClientes.h
    └── gestorClientes.cpp
```

---

## 🚀 **¡MUCHA SUERTE EN TU EXAMEN!**

Recuerda: la clave está en entender el **flujo de datos**:
1. Cliente empaqueta → Envía
2. Servidor recibe → Desempaqueta → Ejecuta → Empaqueta respuesta → Envía
3. Cliente recibe → Desempaqueta → Retorna

**¡Practica mucho y te saldrá perfecto!** 💪
