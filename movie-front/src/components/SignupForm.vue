<template>
  <div>
    <h1>Signup Form</h1>

    <div class="form-group">
      아이디: <input type="text" v-model="username">
    </div>
    <div class="form-group">
      비밀번호: <input type="password" v-model="password">
    </div>

    <button size="lg" variant="success" type="submit"  @submit.prevent="signup">Signup</button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Signup",
  data() {
    return {
      username: "",
      password: ""
    }
  },
  methods: {
    signup() {
      const username = this.username;
      const password = this.password;

      if (!username || !password) {
        return false
      }

      axios
        .post("http://localhost:8000/api/v1/user", { username, password })
        .then(res => {
          if (res.status === 200) {
            // 성공적으로 회원가입이 되었을 경우
            this.$router.push({ name: "Login" })
          }
        })
    }
  }
}
</script>

<style>
</style>