<template>
  <div>
    <!-- Button to Open Modal -->
    <button @click="openModal = true">
      <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" viewBox="0 0 20 20" fill="currentColor">
        <path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z" />
      </svg>
    </button>

    <!-- Modal -->
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-200 rounded-lg shadow-lg p-8 w-full max-w-sm text-violet-950">
      	<div class="flex justify-center">
	        <div class="flex justify-center w-36 h-36 items-center mt-4 rounded-full border-4 border-violet-300 bg-center bg-cover" :style="{ backgroundImage: 'url(' + profImage + ')' }">
	          <label for="imageUpload" class="mt-4 px-2 py-2 h-10 w-10 self-end rounded-full bg-blue-500 text-white cursor-pointer">
	            <svg fill="#000000" height="24px" width="24px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 399.9 399.9" xml:space="preserve">
	              <path d="M366.5,89.1h-24.1l-23.2-50.3c-1.8-3.9-5.8-6.5-10.1-6.5H201.7c-4.3,0-8.3,2.5-10.1,6.5l-23.2,50.3h-49.9V62.4 c0-6.1-5-11.1-11.1-11.1H50.2c-6.1,0-11.1,5-11.1,11.1v26.7h-5.8c-18.4,0-33.3,15-33.3,33.3v211.9c0,18.4,15,33.3,33.3,33.3h333.3 c18.4,0,33.3-15,33.3-33.3V122.4C399.8,104.1,384.8,89.1,366.5,89.1z M208.8,54.6H302l15.9,34.5H192.8L208.8,54.6z M61.2,73.5h35 v15.6h-35V73.5z M366.5,345.4H33.1c-6.1,0-11.1-5-11.1-11.1V227h17.3c6.1,0,11.1-5,11.1-11.1c0-6.1-5-11.1-11.1-11.1H22v-22.2 h39.5c6.1,0,11.1-5,11.1-11.1c0-6.1-5-11.1-11.1-11.1H22v-37.9c0-6.1,5-11.1,11.1-11.1h333.3c6.1,0,11.1,5,11.1,11.1v211.8h0.1 C377.6,340.4,372.6,345.4,366.5,345.4z"/>
				  <path d="M255.4,130.8c-53.8,0-97.6,43.8-97.6,97.6s43.8,97.6,97.6,97.6c53.8,0,97.6-43.8,97.6-97.6 C352.9,174.6,309.1,130.8,255.4,130.8z M255.4,303.7c-41.5,0-75.3-33.8-75.3-75.3s33.8-75.3,75.3-75.3s75.3,33.8,75.3,75.3 C330.7,269.9,296.9,303.7,255.4,303.7z"/>
				  <path d="M255.4,175.3c-29.3,0-53.1,23.8-53.1,53.1s23.8,53.1,53.1,53.1c29.3,0,53.1-23.8,53.1-53.1 C308.5,199.1,284.6,175.3,255.4,175.3z M255.4,259.3c-17,0-30.9-13.9-30.9-30.9s13.9-30.9,30.9-30.9s30.9,13.9,30.9,30.9 S272.4,259.3,255.4,259.3z"/>
				  <path d="M353.8,127.8h-9.9c-6.1,0-11.1,5-11.1,11.1c0,6.1,5,11.1,11.1,11.1h9.9c6.1,0,11.1-5,11.1-11.1 C364.9,132.8,360,127.8,353.8,127.8z"/>
				  <path d="M117.2,138.8c-6.1,0-11.1,5-11.1,11.1v156.9c0,6.1,5,11.1,11.1,11.1c6.1,0,11.1-5,11.1-11.1V149.9 C128.3,143.8,123.3,138.8,117.2,138.8z"/>
				</svg>
	          </label>
	          <input
	            type="file"
	            id="imageUpload"
	            class="hidden"
	            accept="image/*"
	            @change="handleImageChange"
	          />
	          </img>
	        </div>
	    </div>
	    <div class="flex flex-col justify-center">
	    	<h3 class="font-bold text-center">{{ name }}</h3>
	    	<p class="font-thin text-sm text-grey-900 text-center">{{ role }}</p>
	    </div>
	    <div class="flex justify-center gap-2 mt-10 text-sm">
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Logout</button>  
              <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
          </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from '@/stores/auth';
import defaultProfileImage from '@/assets/male.png';

defineProps({
  name: String,
  role: String
});

const authStore = useAuthStore();

const openModal = ref(false);
const profImage = ref(authStore.getUser?.profile_image || defaultProfileImage);
const accessToken = authStore.getAccessToken;

const handleImageChange = async (event) => {
  const file = event.target.files[0];
  
  if (file) {
    // Read the image locally using FileReader
    const reader = new FileReader();
    
    reader.onload = async (e) => {
      profImage.value = e.target.result;
      const formData = new FormData();
      formData.append('profile_image', file);

      try {
        const response = await fetch('http://127.0.0.1:8000/users/update-profile-image/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${accessToken}`, 
          },
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to upload image');
        }

      } catch (error) {
        console.error('Error uploading image:', error);
      }
    };
    reader.readAsDataURL(file);
  }
};
</script>