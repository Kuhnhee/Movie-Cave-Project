<template>
  <form class="col-4 mx-auto">
    <h1>Log in</h1>
    <v-text-field
      v-model="credentials.username"
      label="Username"
      name="Username"
      required
    >
    </v-text-field>
    <v-text-field
      v-model="credentials.password"
      label="password"
      name="Password"
      type="password"
      required
    >
    </v-text-field>
    <br>
    <v-btn light large block @click="login()">Login</v-btn>
  </form>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {},
      passwordRules: [
        (v) => !!v || 'Password is required',
      ],
      usernameRules: [
        (v) => !!v || 'Username is required',
      ],
    }
  },
  methods: {
    login() {
      axios.post('http://localhost:8000/api-token-auth/', this.credentials)
      .then(res => {
        this.$session.start()
        this.$session.set('jwt', res.data.token)
        router.push('/')
      })
    }
  },
}
</script>

<style>
</style>