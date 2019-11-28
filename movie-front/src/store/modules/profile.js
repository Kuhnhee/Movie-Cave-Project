const HOST = process.env.VUE_APP_SERVER_HOST;
const axios = require('axios');

function makeTokenHeader(token) {
    return {'Authorization': `JWT ${token}`}
}

// auth.js  인증관련 모든 State 를 작성.
const state = {
    reviews: [],
    movies: [],
};

const getters = {
};

const mutations = {
    changeReviews (state, reviews) {
        state.reviews = reviews
        sessionStorage.setItem('my_reviews', reviews)
    },
    changeMyMovies (state, movies) {
        state.movies = movies
        sessionStorage.setItem('my_movies', movies)
    },
};

const actions = {
    refreshInfo: ({ commit }, token) => {
        const options = {
            headers: makeTokenHeader(token)
        }
        axios.get(HOST+'/api/v1/my_movies/', options)
            .then(res => {
                commit('changeReviews', res.data.review_set);
                commit('changeMyMovies', res.data.movies);
            })
            .catch(err => console.log(err))
    },

};

export default {
    state, getters, mutations, actions
}
