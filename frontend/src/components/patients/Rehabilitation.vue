<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openRehabilitation" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Patient Rehabilitation Care Form </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getRehabData" class="flex flex-col gap-4">
      			<div class='w-full'>
            		<label for="diagnosis" class="block text-sm text-left mb-2 font-medium">Diagnosis*</label>
            		<input v-model="diagnosis" type="text" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required />
              	</div>
        		<div class='w-full'>
            		<label for="doi" class="block text-sm text-left mb-2 font-medium ">Date of Injury / Condition*</label>
            		<input v-model="doi" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required />
              	</div>
                <div class='w-full'>
                    <label for="type" class="block text-sm text-left mb-2 font-medium ">Type of Injury/Condition*</label>
                    <input v-model="type" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required />
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
    const openRehabilitation = computed(() => modalStore.getRehabilitation);

    const dignosis = ref('');
    const doi = ref('');
    const type = ref('');

    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    };

    async function getRehabData () {
        const backend = "patient/rehabilitation-record";

        if (diagnosis.value && doi.value) { 
            const body = JSON.stringify({
                "diagnosis": diagnosis.value,
                "doi": doi.value,
                "type": type.value,
                "id" : modalStore.getId,
            });

            // poll backend
            const msg = await authStore.APICall({ body: body, api: backend });
            if (msg.success) {
                showAlert(msg.data.message);
                setTimeout(() => {
                    modalStore.reset();
                    //modalStore.prenatalTestModal();
                }, 3000 );              
            } else {
                showAlert(msg.data.error);
            }
        }
    }

</script>