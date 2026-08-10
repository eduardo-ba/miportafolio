// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // URL de producción usada en canonical, alternates y metadatos sociales.
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
