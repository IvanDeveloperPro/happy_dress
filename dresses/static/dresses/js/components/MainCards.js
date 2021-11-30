class MainCards {
    constructor(container, card, counter, api, userAuth,button) {
        this.container = container;
        this.card = card;
        this.userAuth = userAuth;
        this.counter = counter;
        this.target = null;
        this.button = button;
        this._eventUserAuth = this._eventUserAuth.bind(this);

    }
    addEvent() {
        const eventCb = this._access();
        this.container.addEventListener('click', eventCb)
    }
    _access () {
        return this._eventUserAuth;
    }
    _eventUserAuth (e) {
        this.target = e.target.closest('button');
    }
}
