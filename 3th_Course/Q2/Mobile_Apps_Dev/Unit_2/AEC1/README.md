# Unidad2Proyecto - App Android

Proyecto Android base para la práctica de Unidad 2:
- Login / registro con Firebase Authentication
- Lista de productos desde API con Volley
- Favoritos gestionados en Firebase Firestore
- Navegación con fragments

## Cómo usar

1. Abre este proyecto en Android Studio.
2. En `app/build.gradle`, sincroniza dependencias.
3. Agrega tu `google-services.json` en `app/` para Firebase.
4. Ejecuta en un emulador o dispositivo.

## Estructura

- `app/src/main/java/com/example/unidad2proyecto/` — código Kotlin
- `app/src/main/res/layout/` — layouts XML
- `app/src/main/AndroidManifest.xml` — permisos y actividad principal

## Notas

- La URL de la API está en `Constants.kt`.
- Los favoritos se guardan en Firestore bajo `users/{uid}/favorites`.
- Si necesitas adaptar el diseño, edita los archivos XML en `res/layout`.
