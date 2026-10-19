# Luis Eduardo Barrón — Web Developer Portfolio

Portafolio personal multilingüe construido con Astro y TypeScript. Presenta proyectos de desarrollo web, experiencia técnica, stack, formación y datos de contacto en español, inglés y francés.

## Características

- Sitio estático rápido, accesible y responsive.
- Contenido localizado en `es`, `en` y `fr`.
- Componentes reutilizables y datos tipados.
- Imágenes optimizadas con `astro:assets`.
- Canonical, `hreflang`, Open Graph, Twitter Card y datos estructurados.
- CV descargable actualizado al perfil de Web Developer.

## Desarrollo

```sh
npm ci
npm run dev
```

## Verificación y build

```sh
npm run build
```

El resultado estático se genera en `dist/` y está preparado para desplegarse en Netlify.

## Estructura principal

```text
src/
├── components/   # Secciones y elementos de interfaz
├── data/         # Proyectos, habilidades y enlaces
├── i18n/         # Diccionarios ES / EN / FR
├── layouts/      # Documento, navegación y metadatos
├── pages/        # Rutas localizadas
└── styles/       # Sistema visual global
```

El CV se genera desde `scripts/generate_cv.py` y se publica como `public/cv-luis-eduardo-barron.pdf`.


## Entorno reproducible

Usa una versión de Node.js compatible con Astro (`>=22.12.0` según el lockfile) y ejecuta `npm ci` para instalar las versiones de `package-lock.json`. Conserva el lockfile en los commits que cambien dependencias.


## Contribuir y organizar commits

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para crear ramas, escribir commits y verificar los cambios antes de abrir un pull request.

## Verificación automática

El workflow [Build](.github/workflows/build.yml) compila el proyecto en cada pull request y cada actualización de `main`. También puede ejecutarse manualmente desde la pestaña Actions.
