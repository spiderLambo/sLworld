<template>
    <header>
        <nav>
            <ul>
                <li class="pp-menu">
                    <img src="../assets/test/pp.webp" alt="Nom d'utilisateur" class="pp">
                    <ul class="dropdown">
                        <li>Paramètres</li>
                        <li>Se déconnecter</li>
                    </ul>
                </li>
                <li><img src="../../public/sLmusic-big.svg" alt="🎵 sLmusic"></li>
            </ul>
            <ul>
                <li class="ajouter-menu">
                    <h1>Ajouter</h1>
                    <ul class="dropdown">
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

// Style commun pour tous les dropdowns
.dropdown {
  display: none;
  position: absolute;
  top: 100%;
  left: 0;
  border: 1px solid #ccc;
  border-radius: 4px;
  min-width: 120px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  z-index: 10;

  li {
    padding: 8px 16px;
    white-space: nowrap;
    color: #222;
    cursor: pointer;

    &:hover {
      background: #f0f0f0;
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
