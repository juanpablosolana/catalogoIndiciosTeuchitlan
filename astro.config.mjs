import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://juanpablosolana.github.io', // Reemplaza TU-USUARIO con tu nombre de usuario de GitHub
  base: '/catalogoIndiciosTeuchitlan', // Reemplaza con el nombre de tu repositorio (omítelo si es username.github.io)
  output: 'static', // Asegúrate de que sea static para GitHub Pages
});