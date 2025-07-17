<template>
    <section>
        <header>
            <img :src="props.profile" :alt="props.name">
            <h6>{{ props.name }}</h6>

            <input type="range" min="10" v-model="gridEltHeight" max="20" v-if="isGrid">
            
            <div class="menu">
                <input type="checkbox" :id="uniqueId" v-model="isGrid"/>
                <label :for="uniqueId" :class="{ dark: isDark, light: !isDark }">
                    <img :src="isDark ? listDark : listLight"
                    alt="Passer en mode liste">
                    <img :src="isDark ? gridDark : gridLight"
                    alt="Passer en mode liste">
                </label>
            </div>
        </header>

          
        <transition name="fade" mode="out-in">
          <div v-if="!isGrid" class="project-list" key="list">
            <ProjectList 
            v-for="project in props.projects"
            :name="project.name"
            :cover="project.cover"
            :date="project.date"
            :listens="project.listens"
            />
          </div>
          <div v-else class="projects-grid" ref="gridWidth" :style="{ '--grid-cols': gridCols }" key="grid">
            <ProjectGrid 
            :height="gridEltHeight"
            v-for="project in props.projects"
            :name="project.name"
            :cover="project.cover"
            :date="project.date"
            :listens="project.listens"
            />
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

const props = defineProps<{
  name: string,
  profile: string,
  projects: {name: string, cover: string, date: string, listens: number}[]
}>()
</script>


<style scoped lang="scss">
@import '../style';

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
  
  * {
    background-color: transparent;
  }

  > img {
    height: $size;
    width: $size;
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

    // Track (barre)
    &::-webkit-slider-runnable-track {
      height: 8px;
      background: $RangeBG;
      border-radius: 4px;
    }
    &::-moz-range-track {
      height: 8px;
      background: $RangeBG;
      border-radius: 4px;
    }
    &::-ms-fill-lower,
    &::-ms-fill-upper {
      border-radius: 4px;
    }

    // Thumb (curseur)
    &::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: background 0.2s, border 0.2s;
      cursor: pointer;
      margin-top: -8px;
    }
    &::-moz-range-thumb {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      transition: background 0.2s, border 0.2s;
      cursor: pointer;
    }
    &::-ms-thumb {
      width: 24px;
      height: 24px;
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

    label.dark {
      background-color: $dSelectionBg;

      &::after {
        background: $dSelectedElementBg;
      }
    }
    label.light {
      background-color: $lSelectionBg;

      &::after {
        background: $lSelectedElementBg;
      }
    }
    
    label {
      border-radius: 5px;
      display: flex;
      align-items: center;
      gap: $diference;
      padding: calc($diference / 2);
      position: relative;
      cursor: pointer;
      overflow: hidden;
      
      &::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 50%;
        height: 100%;
        background: $lSelectedElementBg;
        transition: .1s;
        border-radius: 5px;
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