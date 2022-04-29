<template>
  <div class="header">
      <h1 v-text="title"></h1>
  </div>
</template>

<script>
export default {
  name: 'MyHeader',
  props: ['title']
}
</script>

<style>
</style>
