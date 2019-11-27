const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');

function makeTokenHeader(token) {
    return {'Aurhorization': `JWT ${token}`}
}

const state = {
    movies: [],
    reviews: [],
};

const getters = {
    getAllMovies (state) {
        return state.Movies;
    },
};

const mutations = {
    pushTodo(state, movie) {
        state.movies.push(movie);
    },
    
    changeMovies (state, movies) {
        state.movies = movies;
    }
};

const actions = {
    refreshTodos: ({ commit }, token) => {
        axios.get(HOST + '/api/v1/my_movies/', makeTokenHeader(token))  // 맨 위에 따로 정의한 함수
            .then(res => {
                commit('changeMovies', res.data);
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
