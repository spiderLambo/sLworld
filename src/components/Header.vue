<template>
    <header>
        <nav>
            <ul>
                <li><img src="../assets/pp.webp" alt="Nom d'utilisateur" class="pp"></li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li>
                  <h1>Ajouter</h1>
                </li>
                <li>
                    <img :src="isDark ? sun : moon"
                        :alt="isDark ? 'Passer au mode jour' : 'Passer au mode nuit'"
                        @click="toggleImage">
                </li>
            </ul>
        </nav>
    </header>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import moon from '../assets/moon-line.svg'
import sun from '../assets/sun-line.svg'

const isDark = ref(true)
const Ajouter = document.querySelector(".add")

function toggleImage() {
  isDark.value = !isDark.value
}

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  isDark.value = savedTheme === 'dark'
  document.body.classList.add(isDark.value ? 'dark' : 'light')
})

watch(isDark, (newVal) => {
  localStorage.setItem('theme', newVal ? 'dark' : 'light')
  document.body.classList.toggle('dark', newVal)
  document.body.classList.toggle('light', !newVal)
})

// Ajouter.addEventListener('onclick', () => {})
</script>

<style lang="scss" scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 75px;
  padding: 0 2rem;

  ul {
    display: flex;
    gap: 20px;
    align-items: center;
  }

  li {
      list-style-type: none;

      &:hover {
        cursor: pointer;
      }

      img {
          height: 24px;
      }
  }
}

.pp {
    height: 40px;
    border-radius: 50%;
}

</style>
