new Vue({
    el: '#app',
    data: {
        mainHeaders: [
            { text: 'Registro', value: 'attendance_record' },
        ],
        attendance_records: [],
        items: [
            {title: 'Home', icon: 'dashboard'},
            {title: 'About', icon: 'question_answer'}
        ],
        type: 'month',
        start: '',
        end: '',
    },

});