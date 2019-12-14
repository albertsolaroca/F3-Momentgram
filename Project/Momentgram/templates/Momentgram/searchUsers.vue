{% extends 'Momentgram/base.html' %}
{% block content %}

{% load static %}
<style>
    .card {
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        max-width: 300px;
        margin: auto;
        text-align: center;
        font-family: arial;
        padding: 20px;
    }

    .title {
        color: grey;
        font-size: 18px;
    }
</style>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<div id="app">
    <div class="search-wrapper">
        <input type="text" v-model="search" placeholder="Search method..." class="searcher"/>
        <div>{{search}}</div>
    </div>
    <div class="row" style="padding-left:30px; padding-right:30px;">
        <div id="v-for-resources" v-for="dict in filteredList">
            {{dict.name}}
            <div class="login-container col-4" style="margin-top: 20px; padding:10px;">
                <div class="card">
                    <h1><a></a></h1>
                    <p class="title"><a></a></p>
                </div>
            </div>

        </div>
    </div>
</div>
<script>
    let app = new Vue({
        el: '#app',
        data: {
            getUsers: [],
            search: 'asdf',
        },
        mounted() {
            let self = this;
            $.ajax({
                url: '../get_users/jbareaco8/',
                method: 'GET',
                success: function (data) {
                    self.getUsers = data.users;
                },
                error: function (error) {
                    console.log("ERROR");
                }
            });
        },

        computed: {
            filteredList() {
                return this.getUsers;
                //.filter(user => {
            //     return user.name.includes(this.search.toLowerCase())
            // })
            }
        }
    });
</script>
{% endblock %}