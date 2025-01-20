import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@lexio': '../../../../rag-ui/dist/rag-ui.es.js'
    }
  }
})
