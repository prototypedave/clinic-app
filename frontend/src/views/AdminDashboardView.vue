<!-- src/views/HomeView.vue -->
<template>
  <div class="flex flex-row text-white max-h-screen">
    <SideBar />
    <div class="flex-1 mx-auto max-w-7xl">
      <AdminHeader />
      <div class="flex m-4">
        <div class="flex-1 grid grid-cols-3 gap-4 max-h-48 text-base">
          <Appointment />
          <Expense />
          <Medicine />
          <Patient />
          <Employee />
          <Note />
          <Payment />
          <SignOut />
          {}
          <div class="col-span-3 w-full bg-white h-44 shadow-2xl text-violet-950 p-4 overflow-y-auto">
            <h3 class="text-center text-lg font-bold mb-4">White Board</h3>
            <div class="space-y-4">
              <!-- Notice Item -->
              <div class="bg-violet-200 p-3 rounded-md shadow-md">
                <p class="text-sm"><strong>John Doe</strong> <span class="text-gray-500 text-xs">at 10:30 AM</span></p>
                <p class="text-gray-800 text-sm mt-1">This is a sample notice message for the whiteboard.</p>
              </div>
              <!-- Notice Item -->
              <div class="bg-violet-200 p-3 rounded-md shadow-md">
                <p class="text-sm"><strong>Jane Smith</strong> <span class="text-gray-500 text-xs">at 11:00 AM</span></p>
                <p class="text-gray-800 text-sm mt-1">Another example notice to display important updates.</p>
              </div>
            </div>
          </div>

        </div>
        <div class="flex-1 ml-8">
          <Calender />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminHeader from '@/components/AdminHeader.vue';
import Calender from '@/components/Calendar.vue';
import SideBar from '@/components/SideBar.vue';
import Appointment from '@/components/modals/AddAppointment.vue';
import Expense from '@/components/modals/AddExpense.vue';

export default {
  components: {
    AdminHeader,
    Calender,
    SideBar,
    Appointment,
    Expense,
  }
}
</script>