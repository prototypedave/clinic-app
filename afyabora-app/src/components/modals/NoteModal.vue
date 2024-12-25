<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <ClipboardDocumentListIcon class="justify-center size-8" aria-hidden="true" />
        <p>Notes</p>
    </button>
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
        <div class="bg-violet-300 text-violet-950 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow">
            <h2 class="text-xl font-bold mb-4 text-center">White Board Messages</h2>
            <form @submit.prevent="submitNote">
                <div>
                    <label class="block text-sm text-left mb-2 font-medium">Note</label>
                    <textarea v-model="Note" type="text" class="mt-1 pl-2 block text-sm w-full border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm" rows="5" required />
                </div>
                <div class="mt-6 flex gap-2 justify-center">
                    <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">submit</button>  
                    <button @click="openModal = false" class="bg-violet-800 hover:violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script setup>
    import { ClipboardDocumentListIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';

    const openModal = ref(false);
    const Note = ref('');
    const alert = ref({ visible: false, message: '' });

    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
            alert.value.visible = false;
        }, 3000); 
    }

    function submitNote() {
        if (Note.value ) {
            showAlert('Note added to notice board');
            openModal.value = true;
            resetForm();
        }
    }

    function resetForm() {
        Note.value = '';
    }
</script>