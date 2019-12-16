<template>
    <v-app>
        <v-app-bar
                app
                color="#212529"
                dark
        >
            <div class="d-flex align-center">
                <v-img
                        alt="Deister Software"
                        class="shrink mr-2"
                        contain
                        src="http://www.deister.net/wp-content/uploads/deister_logo_home_s5.png"
                        transition="scale-transition"
                        height="30px"
                />
                <span class="mr-2">{{apiData.application.doc[0].value[0]}}</span>
            </div>

            <v-spacer></v-spacer>

            <div class="search-wrapper">
                <input type="text" v-model="search" placeholder="Search method..." class="searcher"/>
            </div>
        </v-app-bar>

        <v-content id="v-for-resources" v-for="resource in apiData.application.resources" v-bind:key="resource.base">
            <div class="content">
                <h4 class="ml-8 mr-8 mt-5 title-header">
                    <a class="title title-text">{{resource.base}} </a>
                </h4>
                <div id="v-for-resource" v-for="res in filteredList" v-bind:key="res.path">
                    <v-expansion-panels id="v-for-method" class="pa-2" v-for="method in res.method"
                                        v-bind:key="method.id">
                        <api-resource-component :res="res" :method="method"
                                                :base="resource.base"></api-resource-component>
                    </v-expansion-panels>
                </div>
            </div>
        </v-content>
    </v-app>
</template>

<script>
    import ApiResourceComponent from './components/ApiResourceComponent';
    import apiDataProvider from './ApiDataProvider'
    export default {
        name: 'App',


        components: {
            "api-resource-component": ApiResourceComponent,
        },

        methods: {},

        mounted() {
            apiDataProvider.then(json => this.apiData = json);
        },
        data() {
            return {
                apiData: null,
                search: ''
            }
        },
        computed: {
            filteredList() {
                return this.apiData.application.resources[0].resource.filter(res => {
                    return res.path.toLowerCase().includes(this.search.toLowerCase())
                })
            }
        }
    };
</script>
<style>
    .content {
        width: 100%;
        max-width: 1460px;
        margin: 0 auto;
        padding: 0 20px;
        box-sizing: border-box;
    }

    .v-expansion-panel-content__wrap {
        padding: 0px !important;
    }

    .title-text {
        font-size: 24px !important;
        margin: 0 0 5px !important;
        font-family: sans-serif !important;
        color: #3b4151 !important;
    }

    .title-header {
        padding: 10px 20px 10px 10px !important;
        border-bottom: 1px solid rgba(59, 65, 81, .3);
    }

    .searcher {
        background-color: white;
        color:grey;
        font-size: 14px;
        border-radius: 3px;
        height: 40px;
        width:200px;
        padding: 10px;
    }
    .search-wrapper {
        padding: 5px;
        margin-left: auto;
        width: 33%;
        margin-top: 10px;
        margin-right: auto;
    }
</style>
