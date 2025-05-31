<template>
    <header>
        <nav>
            <ul>
                <li><img src="../assets/test/pp.webp" alt="Nom d'utilisateur" class="pp"></li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li>
                  <h1>Ajouter</h1>
                </li>
                <li>
                    <img :src="isDark ? sun : moon"
                        :alt="isDark ? 'Passer au mode jour' : 'Passer au mode nuit'"
                        @click="toggleTheme">
                </li>
            </ul>
        </nav>
    </header>
</template>

<script setup lang="ts">
import moon from '../assets/moon-line.svg'
import sun from '../assets/sun-line.svg'
import { useTheme } from '../composables/useTheme'


const { isDark, toggleTheme } = useTheme()
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
