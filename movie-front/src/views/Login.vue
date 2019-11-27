<template>
  <v-col id="login">
    <LoginForm />
  </v-col>
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