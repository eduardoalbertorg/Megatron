new Vue({
    el: '#app',
    data: ({
        valid: true,
        username: '',
        username_rules: [
            v => !!v || 'Ingresa el codigo de usuario',
            v => (v && v.length <= 10) || 'Debe de contener menos de 10 caracteres'
        ],
        email: '',
        emailRules: [
            v => !!v || 'E-mail is required',
            v => /.+@.+/.test(v) || 'E-mail must be valid'
        ],
        password: '',
        password_rules: [
            v => !!v || 'Ingresa tu contraseña',
        ],
    }),

    methods: {
        validate() {
            if (this.$refs.form.validate()) {
                this.snackbar = true
            }
        },
        reset() {
            this.$refs.form.reset()
        },
        resetValidation() {
            this.$refs.form.resetValidation()
        }
    }
});