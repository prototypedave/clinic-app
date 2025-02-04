<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openManagement" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Patient Disease Management Form </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getDiseaseData" class="flex flex-col gap-4">
                <h3 class="text-left text-violet-500">Chronic Disease Information</h3>
          		<div class="flex justify-between gap-4">
          			<div class='w-full'>
                		<label for="diagnosis" class="block text-sm text-left mb-2 font-medium">Diagnosis*</label>
                		<input v-model="diagnosis" type="text" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required placeholder="Diabetes, Asthma..."/>
              		</div>
            		<div class='w-full'>
                		<label for="dod" class="block text-sm text-left mb-2 font-medium ">Date of Diagnosis*</label>
                		<input v-model="dod" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required />
              		</div>
                    <div class='w-full'>
                        <label for="severity" class="block text-sm text-left mb-2 font-medium ">Disease Severity*</label>
                        <select v-model="severity" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required >
                            <option value="mild">Mild</option>
                            <option value="moderate">Moderate</option>
                            <option value="Severe">Severe</option>
                        </select>
                    </div>
            	</div>
                <h3 class="text-left text-violet-500 ">Lifestyle Factors</h3>
            	<div class="flex justify-between gap-4">
              		<div class='w-full'>
	                	<label for="smoking" class="block text-sm text-left mb-2 font-medium ">Smoking Status</label>
	                	<textarea v-model="smoking" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm "/>
              		</div>
              		<div class='w-full'>
                		<label for="alcohol" class="block text-sm text-left mb-2 font-medium ">Alcohol Status</label>
                		<textarea v-model="alcohol" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " />
              		</div>
            	</div>
                <div class="flex justify-between gap-4">
                    <div class='w-full'>
                        <label for="physical" class="block text-sm text-left mb-2 font-medium ">Physical Activity</label>
                        <textarea v-model="physical" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm "/>
                    </div>
                    <div class='w-full'>
                        <label for="diet" class="block text-sm text-left mb-2 font-medium ">Diet</label>
                        <textarea v-model="diet" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " />
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
    const openManagement = computed(() => modalStore.getManagement);

    const diagnosis = ref('');
    const dod = ref('');
    const severity = ref('');
    const smoking = ref('');
    const alcohol = ref('');
    const physical = ref('');
    const diet = ref('');

    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    };

    async function getDiseaseData () {
        const backend = "patient/disease-management-record";

        if (complaint.value && onset.value) { 
            const body = JSON.stringify({
                "diagnosis": diagnosis.value,
                "date": date.value,
                "smoking": smoking.value,
                "severity": severity.value,
                "alcohol": alcohol.value,
                "physical" : physical.value,
                "diet" : diet.value,
                "id" : modalStore.getId,
            });

            // poll backend
            const msg = await authStore.APICall({ body: body, api: backend });
            showAlert(msg.data.message);
                
        }
    }

</script>