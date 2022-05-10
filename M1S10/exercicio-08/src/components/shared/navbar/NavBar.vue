<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                    <div class="navbar-nav">
                        <router-link to="/" class="nav-link active" aria-current="page">HOME</router-link>
                        <router-link to="/pessoas/cadastro" class="nav-link active" aria-current="page">CADASTRO</router-link>
                        <router-link to="/pessoas/listagem" class="nav-link active" aria-current="page">LISTAGEM</router-link>
                    </div>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>