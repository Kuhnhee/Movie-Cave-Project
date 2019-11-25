<template>
  <div id="app">
    <v-app id="inspire">
      <v-content>
        <v-container fluid fill-height>
          <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
              <v-card class="elevation-12">
                <v-toolbar color="dark" dark flat>
                  <v-toolbar-title>Login</v-toolbar-title>
                  <v-spacer></v-spacer>
                </v-toolbar>
                <v-card-text>
                  <v-form>
                    <v-text-field 
                      id="usename"
                      label="Username"
                      name="username" 
                      prepend-icon="mdi-account" 
                      type="text" 
                      :rules="usernameRules"
                      v-model="credentials.username"
                      required
                     ></v-text-field>
                    <v-text-field
                      id="password"
                      label="Password"
                      name="password"
                      prepend-icon="mdi-lock"
                      type="password"
                      :rules="passwordRules"
                      v-model="credentials.password"
                      required
                    ></v-text-field>
                  </v-form>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="dark" @click="login">Login</v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: "LoginForm",
  data() {
    return {
      credentials: {
      },
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