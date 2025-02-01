<template>
	<div v-if="openEmergency" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Patient Emergency Form </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getEmergencyData" class="flex flex-col gap-4">
          		<div class="flex justify-between gap-4">
          			<div class='w-full'>
                		<label for="complaint" class="block text-sm text-left mb-2 font-medium ">Chief Complaint*</label>
                		<textarea v-model="complaint" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required placeholder="Describe patient reason for seeking emergency"/>
              		</div>
            		<div class='w-full'>
                		<label for="onset" class="block text-sm text-left mb-2 font-medium ">Onset of Symptoms*</label>
                		<textarea v-model="onset" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required placeholder="date and duration of symptoms"/>
              		</div>
            	</div>
            	<div class="flex justify-between gap-4">
              		<div class='w-full'>
	                	<label for="location" class="block text-sm text-left mb-2 font-medium ">Location of Pain/Symptoms*</label>
	                	<textarea v-model="location" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Left chest...' />
              		</div>
              		<div class='w-full'>
                		<label for="severity" class="block text-sm text-left mb-2 font-medium ">Severity of Pain/Symptoms*</label>
                		<textarea v-model="severity" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Moderate' />
              		</div>
            	</div>
              	<div class="flex justify-between gap-4">	
                	<div class='w-full'>
                  		<label for="character" class="block text-sm text-left mb-2 font-medium ">Character of Pain/Symptoms</label>
                  		<textarea v-model="character" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Sharp, Dull...'/>
                	</div>
                	<div class='w-full'>
                  		<label for="factors" class="block text-sm text-left mb-2 font-medium ">Aggravating/Alleviating Factors</label>
                  		<textarea v-model="factors" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Aggravating/Alleviating Factors' />
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
    const openEmergency = computed(() => modalStore.getEmergency);

    const complaint = ref('');
    const onset = ref('');
    const location = ref('');
    const severity = ref('');
    const character = ref('');
    const factors = ref('');
    const check = ref(false);

    async function getEmergencyData () {
        const backend = "patient/emergency-record";

        if (complaint.value && onset.value) { 
            const body = JSON.stringify({
                "complaint": complaint.value,
                "onset": onset.value,
                "location": location.value,
                "severity": severity.value,
                "character": character.value,
                "factors" : factors.value,
            });

            // poll backend
            const msg = await authStore.APICall({ body: body, api: backend });
            showAlert(msg.message);
            check.value = msg.success;
                
        }

        if (check.value) {
            modalStore.vitalModal();
        }
    }

</script>