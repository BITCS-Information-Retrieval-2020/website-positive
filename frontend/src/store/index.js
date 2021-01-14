import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"


Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    detail: null,
    // total_count: null,
    // tableData: null,
    currentPage: null,
    params: null

  },
  mutations: {
    // saveTableData(state, params) {
    //   state.tableData = params
    // },
    // saveTotal(state, total_count) {
    //   state.total_count = total_count
    // },
    saveDetail(state, detail) {
      state.detail = detail
    },
    saveCurrentPage(state, params) {
      state.currentPage = params
    },
    saveParams(state, params) {
      state.params = params
    }
  },
  getters: {
    myDetail(state) {
      return state.detail
    },
    // myTableData(state) {
    //   return state.tableData
    // },
    // myTotal(state) {
    //   return state.total_count
    // },
    myCurrentPage(state) {
      return state.currentPage
    },
    myParams(state) {
      return state.params
    }
  },
  actions: {},
  modules: {},
  plugins: [createPersistedState()],

})

export default store
