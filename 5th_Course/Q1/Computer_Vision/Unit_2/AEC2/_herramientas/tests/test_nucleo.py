"""Tests del núcleo de la práctica U2."""

from __future__ import annotations

import cv2
import numpy as np
import pytest

import banco_pruebas as bp


def test_entorno_y_hashes():
    assert cv2.__version__.startswith("5.")
    bp.verificar_hashes()


def test_mediana_propia_igual_cv2_en_el_interior():
    rng = np.random.default_rng(1)
    img = rng.integers(0, 256, (96, 96), dtype=np.uint8)
    for k in (3, 5):
        a = bp.mediana_propia(img, k)
        b = cv2.medianBlur(img, k)
        r = k // 2
        assert np.array_equal(a[r:-r, r:-r], b[r:-r, r:-r])


def _naive_hibrida(img: np.ndarray, k: int) -> np.ndarray:
    r = k // 2
    pad = cv2.copyMakeBorder(img, r, r, r, r, cv2.BORDER_REFLECT_101)
    out = np.empty(img.shape, dtype=np.uint8)
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            p = pad[y:y + k, x:x + k]
            cruz = np.concatenate([p[r, :], p[:, r]])
            d1 = p.diagonal()
            d2 = np.fliplr(p).diagonal()
            m1 = np.median(cruz)
            m2 = np.median(np.concatenate([d1, d2]))
            out[y, x] = np.rint(np.median([m1, m2, p[r, r]])).astype(np.uint8)
    return out


def test_hibrida_igual_implementacion_ingenua():
    rng = np.random.default_rng(2)
    img = rng.integers(0, 256, (24, 24), dtype=np.uint8)
    for k in (3, 5):
        assert np.array_equal(bp.mediana_hibrida(img, k), _naive_hibrida(img, k))


def _naive_trim(img: np.ndarray, k: int, alpha: float) -> np.ndarray:
    r = k // 2
    pad = cv2.copyMakeBorder(img, r, r, r, r, cv2.BORDER_REFLECT_101)
    out = np.empty(img.shape, dtype=np.uint8)
    m = int(np.floor(alpha * k * k))
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            v = np.sort(pad[y:y + k, x:x + k].ravel())
            out[y, x] = np.rint(v[m:k * k - m].mean()).astype(np.uint8)
    return out


def test_truncada_igual_ingenua_y_literal_igual_mediana():
    rng = np.random.default_rng(3)
    img = rng.integers(0, 256, (24, 24), dtype=np.uint8)
    for k in (3, 5):
        for alpha in (0.1, 0.2, 0.3, 0.4):
            m = int(np.floor(alpha * k * k))
            if k * k - 2 * m < 1:
                continue
            assert np.array_equal(bp.media_recortada(img, k, alpha), _naive_trim(img, k, alpha))
            assert np.array_equal(
                bp.mediana_truncada_literal(img, k, alpha), bp.mediana_propia(img, k)
            )


def test_rotacion_90_igual_rot90():
    rng = np.random.default_rng(4)
    img = rng.integers(0, 256, (64, 64), dtype=np.uint8)
    H = bp.homografia_rotacion(64, 90)
    warp = cv2.warpPerspective(
        img, H, (64, 64), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=0
    )
    assert np.array_equal(warp, np.rot90(img, k=1))

    H_medio = bp.homografia_rotacion(64, 90, centro_pixel=False)
    warp_medio = cv2.warpPerspective(img, H_medio, (64, 64), flags=cv2.INTER_LINEAR)
    assert not np.array_equal(warp_medio, np.rot90(img, k=1))


def test_identidad_escala_y_gamma():
    rng = np.random.default_rng(6)
    img = rng.integers(0, 256, (128, 128), dtype=np.uint8)
    det = bp.crear_detector("FAST")
    I = np.eye(3)

    for H in (I, bp.homografia_escala(128, 1.0), bp.homografia_rotacion(128, 0)):
        rate, n_orig, n_trans, n_valid = bp.repetibilidad(img, H, det, tol=3.0)
        assert n_orig > 0 and n_trans > 0
        assert rate == pytest.approx(1.0)

    rate, _, _, _ = bp.repetibilidad(img, I, det, tol=3.0, lut=bp.lut_gamma(1.0))
    assert rate == pytest.approx(1.0)


def test_psnr_ssim_conocidos():
    ref = np.zeros((8, 8), np.uint8)
    assert bp.psnr(ref, ref) == float("inf")
    assert bp.psnr(ref, np.full((8, 8), 255, np.uint8)) == pytest.approx(0.0)
    assert bp.psnr(ref, np.ones((8, 8), np.uint8)) == pytest.approx(48.1308, abs=1e-3)
    rng = np.random.default_rng(5)
    img = rng.integers(0, 256, (32, 32), dtype=np.uint8)
    assert bp.ssim(img, img) == pytest.approx(1.0)


def test_ruido_determinista():
    img = np.full((64, 64), 128, np.uint8)
    a = bp.ruido_sal_pimienta(img, 0.10, bp.rng_celda(bp.SEMILLA, 1, 1))
    b = bp.ruido_sal_pimienta(img, 0.10, bp.rng_celda(bp.SEMILLA, 1, 1))
    c = bp.ruido_sal_pimienta(img, 0.10, bp.rng_celda(bp.SEMILLA, 1, 2))
    assert np.array_equal(a, b)
    assert not np.array_equal(a, c)
    fraccion = float((a != img).mean())
    assert 0.07 < fraccion < 0.12

    ga = bp.ruido_gaussiano(img, 20, bp.rng_celda(bp.SEMILLA, 1, 3))
    gb = bp.ruido_gaussiano(img, 20, bp.rng_celda(bp.SEMILLA, 1, 3))
    gc = bp.ruido_gaussiano(img, 20, bp.rng_celda(bp.SEMILLA, 1, 4))
    assert np.array_equal(ga, gb)
    assert not np.array_equal(ga, gc)
    assert 0.8 * 20 < float(ga.std()) < 1.2 * 20


def test_perfil_radial_caja_y_gaussiano():
    lado = 128
    cortes_caja = []
    for k in (3, 5, 9):
        resp = bp.espectro_respuesta("media", {"k": k}, lado)
        perf = bp.perfil_radial(resp)
        corte = bp.frecuencia_corte(perf, lado)
        assert corte > 0
        assert bp.contar_rebotes(perf, 1e-3) > 0
        cortes_caja.append(corte)
    assert cortes_caja[0] > cortes_caja[1] > cortes_caja[2]

    cortes_gauss = []
    for sigma, k in ((0.8, 7), (1.6, 11), (3.0, 19)):
        resp = bp.espectro_respuesta("gaussiano", {"sigma": sigma, "k": k}, lado)
        perf = bp.perfil_radial(resp)
        corte = bp.frecuencia_corte(perf, lado)
        assert corte > 0
        assert bp.contar_rebotes(perf, 1e-3) == 0
        cortes_gauss.append(corte)
    assert cortes_gauss[0] > cortes_gauss[1] > cortes_gauss[2]


def test_puntuar_bordes():
    ref = np.zeros((64, 64), np.uint8)
    ref[32, :] = 1
    precision, recall, f1, px = bp.puntuar_bordes(ref, ref, tol=2)
    assert (precision, recall, f1, px) == (1.0, 1.0, 1.0, 64)

    det = np.zeros((64, 64), np.uint8)
    det[35, :] = 1
    precision, recall, f1, px = bp.puntuar_bordes(det, ref, tol=2)
    assert (precision, recall, f1) == (0.0, 0.0, 0.0)


def test_escena_sintetica():
    img, ref = bp.crear_escena_sintetica()
    assert img.shape == (512, 512) and img.dtype == np.uint8
    assert ref.sum() > 0
    assert img[100, 100] == 210
    assert img[100, 350] == 50
    assert img[270, 255] == 150
    assert ref[50, 100] == 1
    assert img[400, 400] == 128


def test_repetibilidad_90_homografia_vs_rot90():
    rng = np.random.default_rng(7)
    img = rng.integers(0, 256, (96, 96), dtype=np.uint8)
    lado = img.shape[0]
    H = bp.homografia_rotacion(lado, 90)
    det = bp.crear_detector("FAST")
    rate_h, n_orig, n_trans, n_valid = bp.repetibilidad(img, H, det, tol=3.0)
    assert n_orig > 0 and n_trans > 0 and n_valid > 0

    img_rot = np.rot90(img, k=1)
    kp_orig = det.detect(img, None)
    kp_rot = det.detect(img_rot, None)
    pts = np.float32([kp.pt for kp in kp_orig]).reshape(-1, 1, 2)
    proj = cv2.perspectiveTransform(pts, H).reshape(-1, 2)
    dentro = (
        (proj[:, 0] >= 0)
        & (proj[:, 0] < lado)
        & (proj[:, 1] >= 0)
        & (proj[:, 1] < lado)
    )
    proj = proj[dentro]
    pts_rot = np.float32([kp.pt for kp in kp_rot]).reshape(-1, 2)
    dist = np.linalg.norm(proj[:, None, :] - pts_rot[None, :, :], axis=2)
    rate_rot = float((dist.min(axis=1) <= 3.0).sum()) / len(proj)
    assert rate_rot == pytest.approx(rate_h)
