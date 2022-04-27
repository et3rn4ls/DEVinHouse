class Validations {
    validarCampoObrigatorio(attr) {
        if (!attr) {
            return 'Este campo é obrigatório!'
        }
        return true
    }

    validarCampoValor(valor) {
        if (valor <= 0) {
            return 'O valor precisa ser maior que zero!'
        }
        return true
    }
}

export default new Validations()
