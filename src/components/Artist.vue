<template>
    <section>
        <header>
            <img src="../assets/test/artist.jpeg" alt="PLK">
            <h6>PLK</h6>

            <input type="range" min="10" v-model="gridEltHeight" max="20" v-if="isGrid">
            
            <div class="menu">
                <input type="checkbox" :id="uniqueId" v-model="isGrid"/>
                <label :for="uniqueId">
                    <img :src="isDark ? listDark : listLight"
                    alt="Passer en mode liste">
                    <img :src="isDark ? gridDark : gridLight"
                    alt="Passer en mode liste">
                </label>
            </div>
        </header>

          
        <transition name="fade" mode="out-in">
          <div v-if="!isGrid" class="project-list" key="list">
            <ProjectList />
            <ProjectList />
          </div>
          <div v-else class="projects-grid" ref="gridWidth" :style="{ '--grid-cols': gridCols }" key="grid">
            <ProjectGrid :height="gridEltHeight" />
            <ProjectGrid :height="gridEltHeight"/>
          </div>
        </transition>
    </section>
</template>



<script setup lang="ts">
import { ref, computed } from 'vue'
import { useTheme } from '../composables/useTheme'
import listLight from '../assets/list-light.svg'
import listDark from '../assets/list-dark.svg'
import gridLight from '../assets/grid-light.svg'
import gridDark from '../assets/grid-dark.svg'

import ProjectList from './ProjectList.vue'
import ProjectGrid from './ProjectGrid.vue'

const { isDark } = useTheme()

const isGrid = ref(false)
const gridEltHeight = ref(15)
const uniqueId = `switch-${Math.random().toString(36).substr(2, 9)}`

let gridCols =  computed(() => {
  if (gridEltHeight.value <= 10) {
    return 7
  } else if (gridEltHeight.value <= 12) {
    return 6
  } else if (gridEltHeight.value <= 13) {
    return 5
  } else if (gridEltHeight.value <= 16) {
    return 4
  } else if (gridEltHeight.value <= 19) {
    return 3
  } else {
    return 2
  }
})


</script>


<style scoped lang="scss">
$size: 25px;
$diference: 5px;

section {
  border: 3px solid;
  border-radius: 10px;
  width: 95vw;
  max-width: 95vw;
  overflow: hidden;
}

header {
  box-sizing: border-box;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 1rem;
  gap: 1vw;
  height: auto;
  width: 100%;


  > img {
    height: $size;
    border-radius: 50%;
  }

  h6 {
    font-size: $size;
  }

  input {
    margin-left: auto;
    
    width: 200px;
    height: 2.2em;
    background: transparent;
    accent-color: #007bff; // fallback moderne

    // Track (barre)
    &::-webkit-slider-runnable-track {
      height: 8px;
      background: linear-gradient(90deg, #007bff 0%, #b3d4fc 100%);
      border-radius: 4px;
    }
    &::-moz-range-track {
      height: 8px;
      background: linear-gradient(90deg, #007bff 0%, #b3d4fc 100%);
      border-radius: 4px;
    }
    &::-ms-fill-lower,
    &::-ms-fill-upper {
      background: #b3d4fc;
      border-radius: 4px;
    }

    // Thumb (curseur)
    &::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 24px;
      height: 24px;
      background: #fff;
      border: 3px solid #007bff;
      border-radius: 50%;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: background 0.2s, border 0.2s;
      cursor: pointer;
      margin-top: -8px; // pour centrer le thumb sur la track
    }
    &::-webkit-slider-thumb:hover {
      background: #007bff;
      border-color: #0056b3;
    }
    &::-moz-range-thumb {
      width: 24px;
      height: 24px;
      background: #fff;
      border: 3px solid #007bff;
      border-radius: 50%;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: background 0.2s, border 0.2s;
      cursor: pointer;
    }
    &::-moz-range-thumb:hover {
      background: #007bff;
      border-color: #0056b3;
    }
    &::-ms-thumb {
      width: 24px;
      height: 24px;
      background: #fff;
      border: 3px solid #007bff;
      border-radius: 50%;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: background 0.2s, border 0.2s;
      cursor: pointer;
    }

    // Remove outline on focus
    &:focus {
      outline: none;
    }

    // Pour Firefox
    &::-moz-focus-outer {
      border: 0;
    }
  }

  &:not(:has(input[type="range"])) .menu {
    margin-left: auto;
  }

  .menu {
    position: relative;
    display: flex;
    align-items: center;

    input[type="checkbox"] {
      height: 0;
      width: 0;
      visibility: hidden;
    }

    label {
      display: flex;
      align-items: center;
      gap: $diference;
      padding: calc($diference / 2);
      position: relative;
      border: 1px solid;
      border-radius: 5px;
      cursor: pointer;
      overflow: hidden;

      &::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 50%;
        height: 100%;
        background: blue;
        transition: .1s;
        z-index: 0;
      }

      img {
        z-index: 1;
        height: calc($size - $diference);
        position: relative;
        background: none;
      }

      &:active::after {
        width: 60%;
      }
    }

    input:checked + label::after {
      left: 100%;
      transform: translateX(-100%);
    }
  }
}

// List
.project-list {
  display: flex;
  flex-direction: column;
}

// Grid
.projects-grid {
  border-top: 3px solid;
  display: grid;
  grid-template-columns: repeat(var(--grid-cols), 1fr);
  gap: 2vw;
  padding: 1vw;
  width: 100%;
}

// Transitions
.fade-enter-active, .fade-leave-active {
  transition: opacity .3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>