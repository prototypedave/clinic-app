<template>

    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <ArrowLeftStartOnRectangleIcon class="justify-center size-8" aria-hidden="true" />
        <p>LogOut</p>
    </button>
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
        <div class="bg-violet-300 text-violet-950 rounded-lg shadow-lg p-8 w-full max-w-sm shadow">
            <h2 class="text-xl font-bold mb-4 text-center">Sign out ?</h2>
            <div class="mt-6 flex gap-6 justify-center">
                <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Yes</button>  
                <button @click="openModal = false" class="bg-violet-800 hover:violet-950 text-white font-bold py-2 px-4 rounded-md">No</button>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ArrowLeftStartOnRectangleIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';

    const openModal = ref(false);

</script>