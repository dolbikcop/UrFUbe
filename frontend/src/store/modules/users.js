import axios from 'axios';

const state = {
    is_auth: false
};

const getters = {
    is_authorised: state => state.is_auth
};

const actions = {
    get_video: async function ({getters}, params) {
        if (!getters.is_authorised) {
            return await axios.get(`video/${params.video_id}`, {params: params})
        } else {
            return await axios.get(`auth/video/${params.video_id}`, {params: params})
        }
    },
    registration: async function ({dispatch}, json) {
        return await axios.post('auth/register', json, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(async (r) => {
            if (!!r && r.status === 201) {
              let obj = {
                username: json.email,
                password: json.password
              }
                await dispatch('login', obj);
            }
        })
    },
    login: async function ({commit}, obj) {
        let r = await axios.post('auth/login', obj, {
            headers: {
                'access': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded'
            }});
        if (r && r.status === 204) {
            commit('set_auth');
        }
        return r;
    },
    upload: async function (form) {
        await axios.post(`video/upload`, form);
    },
    async account_me({state}) {
        let {data} = await axios.get(`user`);
        return data;
    },
    async get_user({}, form) {
        console.log(form)
        return await axios.get(`user/${form.user_id}`, form)
    },
    async logOut({commit}) {
        await axios.post('auth/logout');
        commit('logout');
    }
};

const mutations = {
    set_auth(state) {
        state.is_auth = true;
    },
    logout({state}) {
        state.is_auth = false;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};