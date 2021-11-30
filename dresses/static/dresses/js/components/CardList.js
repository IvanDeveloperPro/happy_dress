class CardList extends MainCards {
    _eventUserAuth (e) {
        super._eventUserAuth(e);
        if (this.target && this.target.name === 'purchases') {
            this._eventPurchases(this.target)
        }
    }
    _eventPurchases  (target)  {
        const cardId = target.closest(this.card).getAttribute('data-id');
        if(target.hasAttribute('data-out')) {
            this.button.purchases.addPurchases(target,cardId, this.counter.plusCounter)
        } else {
            this.button.purchases.removePurchases(target,cardId,this.counter.minusCounter);

        }
    }
}
