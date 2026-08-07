// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // URL de producción (Netlify). Necesaria para canonical y og:url.
  // ⚠️ Cambiar por el subdominio real que asigne Netlify, o por el dominio propio.
  site: 'https://miportafolio.netlify.app',

  // `/` = español (sin prefijo), `/en/` y `/fr/` para los demás.
  i18n: {
    defaultLocale: 'es',
    locales: ['es', 'en', 'fr'],
    routing: { prefixDefaultLocale: false }
  },

  vite: {
    plugins: [tailwindcss()]
  }
});
