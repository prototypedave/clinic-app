<template>
	<div v-if="openRegister" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Additional Patient Details </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getPatientInfo" class="flex flex-col gap-4">
          		<div class="flex justify-between gap-4">
          			<div class='w-full'>
                		<label for="email" class="block text-sm text-left mb-2 font-medium ">Email</label>
                		<input v-model="email" type="email" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm "/>
              		</div>
            		<div class='w-full'>
                		<label for="dob" class="block text-sm text-left mb-2 font-medium ">Date of Birth*</label>
                		<input v-model="dob" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required/>
              		</div>
              		<div class='w-full'>
                		<label for="gender" class="block text-sm text-left mb-2 font-medium ">Gender*</label>
                		<select v-model="gender" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required >
                  			<option value='male'>Male</option>
                  			<option value='female'>Female</option>
                		</select>
              		</div>
            	</div>
            	<div>
                	<label for="address" class="block text-sm text-left mb-2 font-medium ">Address</label>
                	<input v-model="address" type="text" class="mt-1 pl-2 block  text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Kangemi'/>
              	</div>
            	<p class="text-center text-violet-500 mb-4"> Fill below if patient has insuarance </p>
            	<div class="flex justify-between gap-4">
              		<div>
                		<label for="provider" class="block text-sm text-left mb-2 font-medium ">Insurance Provider</label>
                		<input v-model="provider" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='NHIF'/>
              		</div>
              		<div>
                		<label for="policy" class="block text-sm text-left mb-2 font-medium ">Policy Number</label>
                		<input v-model="policy" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Policy Number'/>
              		</div>
            	</div>
              	<div class="flex justify-between gap-4">
                	<div>
                  		<label for="group" class="block text-sm text-left mb-2 font-medium ">Group Number</label>
                  		<input v-model="group" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Group Number' />
                	</div>
                	<div>
                  		<label for="first" class="block text-sm text-left mb-2 font-medium ">Child First Name</label>
                  		<input v-model="first" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='First Name'/>
                	</div>
                	<div>
                  		<label for="last" class="block text-sm text-left mb-2 font-medium ">Last Name</label>
                  		<input v-model="last" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='+254' />
                	</div>
              	</div>
	            <div class="flex justify-end gap-4 h-10">
		            <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-secondary-btn-fcs">back</button>
		            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
		        </div>
        	</form>
      	</div>
    </div>
</template>

<script setup>
	import { ref } from 'vue';
    import { useAuthStore } from '@/stores/auth';
    import { usePatientModalStore } from '@/stores/patientModal';
    import { computed } from 'vue';

    const authStore = useAuthStore();
    const modalStore = usePatientModalStore();
    const openRegister = computed(() => modalStore.getRegister);

</script>