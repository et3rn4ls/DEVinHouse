<template>
    <div class="app">
        <NavBar />
        <hr>
        <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/shared/navbar/NavBar';

export default {
    name: 'App',
    components: {
        NavBar
    }
}
</script>

<style>

</style>
