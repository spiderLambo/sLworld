<template>
    <header>
        <nav>
            <ul>
                <li class="pp-menu">
                    <img src="../assets/test/pp.webp" alt="Nom d'utilisateur" class="pp">
                    <ul :class="['dropdown', isDark ? 'dark' : 'light']">
                        <li>Paramètres</li>
                        <li class="end">Se déconnecter</li>
                    </ul>
                </li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li class="ajouter-menu">
                    <h1>Ajouter</h1>
                    <ul :class="['dropdown', isDark ? 'dark' : 'light']">
                      <li>Artiste</li>
                      <li>Projet</li>
                    </ul>
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

.dropdown.light {
  li:hover {
    color: #ddd;
    background: #0f0f0f;
  }

  .end,
  .end:hover {
    color: rgb(255, 46, 46);
  }
}

.dropdown.dark {
  li:hover {
    color: #222;
    background: #f0f0f0;
  }

  .end,
  .end:hover {
    color: rgb(255, 46, 46);
  }
}


.dropdown {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  border: 1px solid #333;
  border-radius: 4px;
  min-width: 120px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  z-index: 10;
  overflow: hidden;
  



  li {
    padding: 8px 16px;
    white-space: nowrap;
    cursor: pointer;


    &:hover {
      text-decoration: underline;
    }
  }
}

// Spécifique à la pp-menu (largeur différente)
.pp-menu .dropdown {
  min-width: 140px;
}

// Positionnement relatif pour les menus qui contiennent un dropdown
.ajouter-menu,
.pp-menu {
  position: relative;

  &:hover > .dropdown {
    display: block;
  }
}
</style>
