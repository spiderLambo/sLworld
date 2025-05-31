import { ref, watch } from 'vue'

const isDark = ref(localStorage.getItem('theme') === 'dark')


function toggleTheme() {
  isDark.value = !isDark.value
}


watch(isDark, (newVal) => {
  localStorage.setItem('theme', newVal ? 'dark' : 'light')
  document.body.classList.toggle('dark', newVal)
  document.body.classList.toggle('light', !newVal)
}, { immediate: true })

export function useTheme() {
  return {
    isDark,
    toggleTheme,
  }
}
