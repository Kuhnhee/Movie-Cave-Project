<template>
  <div id="login">
    <h1>Log in</h1>
    <br>
    <LoginForm />
  </div>
</template>

<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
  name: 'login',
  components: {
    LoginForm,
  },
  
}
</script>

<style>
</style>