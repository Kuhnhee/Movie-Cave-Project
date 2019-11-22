<template>
  <div>

    <div class="form-group">
      <label for="id">아이디</label>
      <input v-model="credentials.username" type="text" id="id" class="form-control" placeholder="아이디를 입력해주세요.">
    </div>

    <div class="form-group">
      <label for="id">비밀번호</label>
      <input v-model="credentials.password" type="password" id="password" class="form-control" placeholder="비밀번호를 입력해주세요.">
    </div>

    <button @click="login()" class="btn btn-primary">로그인</button>

  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {},
    }
  },
  methods: {
    login() {
      // console.log(this.credentials)
      axios.post('http://localhost:8000/api-token-auth/', this.credentials)
      .then(res => {
        // console.log(res.data.token)
        this.$session.start()
        this.$session.set('jwt', res.data.token)
        router.push('/')
      })
    },
  },
}
</script>

<style>

</style>