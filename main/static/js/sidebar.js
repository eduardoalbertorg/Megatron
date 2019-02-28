var main_vue = new Vue({
    el: '#side_bar',
    type: 'month',
    start: '',
    end: '',
    data: {
        items: [
            {title: 'Home', icon: 'dashboard'},
            {title: 'About', icon: 'question_answer'}
        ],
        type: 'month',
        start: '',
        end: '',
    }
});