<template>
    <div v-if="alert.visible" class="fixed top-4 right-4 bg-violet-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
	<div v-if="openScheduled" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      	<div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        	<h2 class="text-xl font-bold mb-4 text-center"> Patient Appointment Form </h2>
        	<p class="text-center text-violet-500 mb-4"> Please fill in all the required fields * </p>
        	<form @submit.prevent="getAppointmentData" class="flex flex-col gap-4">
          		<div class="flex justify-between gap-4">
                    <p v-if="dateMessage" class="text-sm text-red-500 mt-1">{{ dateMessage }}</p> 
                    <div class='w-full'>
                        <label for="type" class="block text-sm text-left mb-2 font-medium ">Appointment Type*</label>
                        <select v-model="type" type="text" class="mt-1 pl-2 block w-full text-sm py-1 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                            <option value="new patient">New Patient</option>
                            <option value="follow up">Follow Up</option>
                            <option value="consultation">Consultation</option>
                        </select> 
                    </div>
          			<div class='w-full'>
                		<label for="date" class="block text-sm text-left mb-2 font-medium ">Appointment Date*</label>
                		<input v-model="date" type="date" class="mt-1 pl-2 block w-full text-sm py-2 bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" required :min="minDate" @change='disableDate'/>
              		</div>
            	</div>
                <p v-if="notifyMessage" class="text-sm text-red-500 mt-1">{{ notifyMessage }}</p>
            	<div class="flex justify-between gap-4">
              		<div class='w-full'>
                        <label for="start" class="block text-sm text-left mb-2 font-medium ">Start time*</label>
                        <input v-model="start" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required :disabled="!date" @input="validateStartTime"/>
                    </div>
                    <div class='w-full'>
                        <label for="end" class="block text-sm text-left mb-2 font-medium ">End time*</label>
                        <input v-model="end" type="time" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required :disabled="!date || !start" @input="validateEndTime"/>
                    </div>            		
            	</div> 
                <div class="flex justify-between gap-4">
                    <div class='w-full'>
                        <label for="reason" class="block text-sm text-left mb-2 font-medium ">Reason for appointment*</label>
                        <textarea v-model="reason" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Brief description for booking an appointment'/>
                    </div>
                    <div class='w-full'>
                        <label for="reference" class="block text-sm text-left mb-2 font-medium ">Referred By</label>
                        <input v-model="reference" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Reference name'/>
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
    import { useCalendarStore } from '@/stores/calendarStore';
    import { computed } from 'vue';

    const authStore = useAuthStore();
    const modalStore = usePatientModalStore();
    const eventStore = useCalendarStore();
    const openScheduled = computed(() => modalStore.getScheduled);

    const date = ref('');
    const start = ref('');
    const end = ref('');
    const type = ref('');
    const reference = ref('');
    const reason = ref('');
    const check = ref(false);

    const notifyMessage = ref('');
    const dateMessage = ref('');

    const events = ref([
        { id: 1, start: '2025-02-08 07:00', end: '2025-02-08 21:00', title: 'David', calendarId: 'patient' },
        { id: 2, start: '2025-02-28 08:00', end: '2025-02-28 10:00', title: 'Alfonso', calendarId: 'patient' },
        { id: 3, start: '2025-02-28 10:00', end: '2025-02-28 11:00', title: 'Alfonso', calendarId: 'patient' },
    ]);

    const minDate = new Date().toISOString().split("T")[0];

    function parseTimeToMinutes(time) {
        const [hours, minutes] = time.split(':').map(Number);
        return hours * 60 + minutes;
    };

    function getAvailableSlots(date) {
        const dayEvents = events.value.filter((event) => event.start.startsWith(date));
        dayEvents.sort((a, b) => new Date(a.start) - new Date(b.start));

        const slots = [];
        let previousEnd = parseTimeToMinutes('07:00'); 

        dayEvents.forEach((event) => {
            const eventStart = parseTimeToMinutes(event.start.slice(11));
            const eventEnd = parseTimeToMinutes(event.end.slice(11));

            if (eventStart > previousEnd) {
                slots.push({ start: previousEnd, end: eventStart });
            }
            previousEnd = Math.max(previousEnd, eventEnd);
        });

        const endOfDay = parseTimeToMinutes('20:59');
        if (previousEnd < endOfDay) {
            slots.push({ start: previousEnd, end: endOfDay });
        }

        return slots;
    };

    function validateStartTime () {
        const slots = getAvailableSlots(date.value);
        const selectedMinutes = parseTimeToMinutes(start.value);
        const isValid = slots.some((slot) => selectedMinutes >= slot.start && selectedMinutes <= slot.end);

        if (isValid) {
            notifyMessage.value = ''; 
        } else {
            notifyMessage.value = `Unavailable time slot, try another slot`;
        }
    };

    function validateEndTime () {
        const slots = getAvailableSlots(date.value);
        const endMinutes = parseTimeToMinutes(end.value);
        const startMinutes = parseTimeToMinutes(start.value);
        const isValid = slots.some((slot) => endMinutes >= slot.start && endMinutes <= slot.end && endMinutes > (startMinutes + 15));

        if (isValid) {
            notifyMessage.value = '';
        } else {
            notifyMessage.value = 'Appointment should be 15 minutes or more';
        }
    };

    function isDayFullyBooked(date) {
        const dayEvents = events.value.filter(event => event.start.startsWith(date));
        dayEvents.sort((a, b) => new Date(a.start) - new Date(b.start));

        let previousEnd = parseTimeToMinutes("07:00"); 

        for (const event of dayEvents) {
            const eventStart = parseTimeToMinutes(event.start.slice(11));
            const eventEnd = parseTimeToMinutes(event.end.slice(11));

            if (eventStart > previousEnd) {
                return false;
            }
        previousEnd = Math.max(previousEnd, eventEnd);
        }

        return previousEnd >= parseTimeToMinutes("20:59");
    };


    function disableDate () {
        if (isDayFullyBooked(date.value)) {
            dateMessage.value = 'Fully booked date or Physician absent on this date';
            date.value = '';
        } else {
            dateMessage.value = '';
        }
    };
    
    const alert = ref({ visible: false, message: '' });
    const error = ref("");
    
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    };

    async function getAppointmentData () {
        const backend = "patient/appointment-record";
        if (end.value && start.value) {
            const body = JSON.stringify({
                "id" : modalStore.getId,
                "start" : `${date.value} ${start.value}`,
                "end" : `${date.value} ${end.value}`,
                "type" : type.value,
                "reason" : reason.value,
            });

            const msg = await authStore.APICall({ body: body, api: backend });
                showAlert(msg.data.message);
                await eventStore.getEvents(authStore.getAccessToken);
                setTimeout(() => {
                    modalStore.reset();
                    reset();
                }, 3000);     
        }
        
    }

    function reset () {
        date.value = '';
        start.value = '';
        end.value = '';
        type.value = '';
        reference.value = '';
        reason.value = '';
        check.value = false;

    }

</script>