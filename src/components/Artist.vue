<template>
    <section>
        <header>
            <img src="../assets/test/artist.jpeg" alt="PLK">
            <h6>PLK</h6>
            
            <div class="menu">
                <input type="checkbox" id="switch" />
                <label for="switch">
                    <img :src="isDark ? listDark : listLight"
                    alt="Passer en mode liste">
                    <img :src="isDark ? gridDark : gridLight"
                    alt="Passer en mode liste">

                </label>
            </div>
        </header>
    </section>
</template>



<script setup lang="ts">
import { useTheme } from '../composables/useTheme'
import listLight from '../assets/list-light.svg'
import listDark from '../assets/list-dark.svg'
import gridLight from '../assets/grid-light.svg'
import gridDark from '../assets/grid-dark.svg'


const { isDark, toggleTheme } = useTheme()
</script>



<style scoped lang="scss">
$size: 25px;
$diference: 5px;

section {
  border: 3px solid;
  border-radius: 10px;
  padding: 1rem;
  width: 95vw;
}

header {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 1vw;
  height: calc($size + 2 * $diference);
  width: 100%;

  > img {
    height: $size;
    border-radius: 50%;
  }

  h6 {
    font-size: $size;
  }

  .menu {
    position: relative;
    margin-left: auto;
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
</style>