var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i < updateBtns.length; i++){
	updateBtns[i].addEventListener('click', function(){
		var speciesId = this.dataset.species
		var action = this.dataset.action
		console.log('speciesId:', speciesId, 'action:', action)

		console.log('User:', user)
		if(user === 'AnonymousUser'){
			console.log('Not logged in')
		}else{
			updateUserOrder(speciesId, action)
		}
	})
}

function updateUserOrder(speciesId, action){
	console.log('User is authenticated, sending data...')

	var url = '/update_item/'

	fetch(url, {
		method:'POST',
		headers:{
			'Content-Type':'application/json',
			'X-CSRFToken':csrftoken,
		},
		body:JSON.stringify({'speciesId': speciesId, 'action':action})
	})

	.then(response =>{
		return response.json()
	}) 

	.then(data =>{
		console.log('data:', data)
	}) 
}