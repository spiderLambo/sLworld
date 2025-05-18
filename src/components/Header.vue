<template>
    <header>
        <nav>
            <ul>
                <li><img src="../assets/pp.webp" alt="Nom d'utilisateur" class="pp"></li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li class="add">
                  <h1>Ajouter</h1>
                  <ul>
                    <li>Ajouter un artiste</li>
                    <li>Ajouter un projet</li>
                  </ul>
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
.add {
  // h1 {
    // &:hover + ul {
      // }
      // }
  ul {
    position: absolute;
    display: flex;
    flex-direction: column;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    box-shadow: 1px 1px 1px #000,
    -1px 1px 1px #000;
    // display: none;
  }
}
</style>
