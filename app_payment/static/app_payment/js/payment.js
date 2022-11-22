const stripe = Stripe('pk_test_TYooMQauvdEDq54NiTphI7jx');
const buyButton = document.getElementById('buy-button');
const itemid = buyButton.getAttribute('itemid');

buyButton.addEventListener('click', function() {
    fetch(`/buy/${itemid}`, {method: 'GET'})
        .then(response => response.json())
        .then((session) => {
            if (session.error) {
                console.log('error:', session.error);
            } else {
                return stripe.redirectToCheckout({ sessionId: session.sessionId })
            }
        })
});
