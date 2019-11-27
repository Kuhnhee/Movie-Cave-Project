const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');

function makeTokenHeader(token) {
    return {'Aurhorization': `JWT ${token}`}
}

// auth.js  인증관련 모든 State 를 작성.
const state = {
    movies: [],
};

const getters = {
    getAllMovies (state) {
        return state.Movies;
    },
    getFinishedTodos(state) {
        return state.todos.filter(todo => todo.completed)
    },
    getLeftTodos(state) {
        return state.todos.filter(todo => !todo.completed)
    }
};

const mutations = {
    pushTodo(state, todo) {
        state.todos.push(todo);
    },
    
    changeTodos (state, todos) {
        state.todos = todos;
    }
};

const actions = {
    refreshTodos: ({ commit }, token) => {
        axios.get(HOST + '/api/v1/my_movies/', makeTokenHeader(token))  // 맨 위에 따로 정의한 함수
            .then(res => {
                commit('changeTodos', res.data);
            })
            .catch(err => console.error(err));
    },

    addTodo: ({ commit }, todo, token) => {
        axios.post(HOST + '/api/v1/todos/', todo, makeTokenHeader(token))
            .then(res => commit('pushTodo', res.data))
            .catch(err => console.error(err))
    },

    removeTodo: (_, todoId, token) => {
        axios.delete(HOST + `/api/v1/todos/${todoId}`, makeTokenHeader(token))
            // .then(_ => this.refreshTodos(token))
            .catch(err => console.error(err))
    }
};

export default {
    state, getters, mutations, actions
}
