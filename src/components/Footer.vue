<template>
    <footer>
        <label for="sort"></label>
        <select id="sort">
            <option value="">Trier par</option>
            <option value="Ajouté recemment">Ajouté recemment</option>
            <option value="A-Z">A-Z</option>
            <option value="Z-A">Z-A</option>
        </select>
    </footer>
</template>

<script setup lang="ts"></script>

<style lang="scss" scoped>
footer {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;

    label {
        margin-right: auto;
        font-weight: bold;
    }

    select {
        padding: 5px;
        border-radius: 4px;
        cursor: pointer;

        &:focus {
            outline: none;
            border-color: #80bdff;
        }
    }
}
</style>