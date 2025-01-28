<template>
    <div 
        v-if="alert.visible" 
        class="fixed top-4 right-4 bg-green-500 text-white p-4 rounded-md shadow-lg z-50">
        {{ alert.message }}
    </div>
    <button class="flex flex-col p-4 bg-violet-800 justify-between items-center text-white hover:bg-violet-950 rounded-md" @click="openModal = true">
        <UserIcon class="justify-center size-8" aria-hidden="true" />
        <p>Patient</p>
    </button>
    
    <!-- check patient -->
    <div v-if="openModal" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-xl shadow text-violet-950">        
        
        <!-- Patient Intro Form -->
        <h2 class="text-xl font-bold mb-1 text-center"> Patient Details Form </h2>
        <p class="text-center text-violet-500 text-sm mb-4"> Please fill all details accordingly </p>
        <form @submit.prevent="LookUpPatient" class="flex flex-col gap-4">
          <div class="flex gap-4">
            <div>
              <label for="first" class="block text-sm text-left mb-2 font-medium">First Name*</label>
              <input v-model="first" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='First Name' required />
            </div>
            <div>
              <label for="second" class="block text-sm text-left mb-2 font-medium ">Middle Name</label>
              <input v-model="second" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Second Name' />
            </div>
            <div>
              <label for="last" class="block text-sm text-left mb-2 font-medium ">Last Name*</label>
              <input v-model="last" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Last Name' required />
            </div>
          </div>
          <div class="flex gap-4">
            <div>
              <label for="mobile" class="block text-sm text-left mb-2 font-medium ">Telephone*</label>
              <input v-model="mobile" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='+254' required />
            </div>
            <div>
              <label for="reason" class="block text-sm text-left mb-2 font-medium ">Select Purpose of the visit*</label>
              <select v-model="reason" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="emergency">Urgent/Emergency</option>
                <option value="scheduled care">Scheduled Care</option>
                <option value="disease management">Disease Management</option>
                <option value="maternity care">Maternity Care</option>
                <option value="rehabilitation">Rehabilitation</option>
                <option value="palliative care">Palliative Care</option>
                <option value="consultation">Consultation</option>
              </select> 
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openModal = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">close</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>

        </form>
      </div>
    </div>

    <!-- Patient Symptoms -->
    <div v-if="openPatientSymptoms" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Patient Symptoms Data </h2>
        <p class="text-center text-sm mb-4 text-violet-500"> Please fill in all the required fields * </p>
        <form @submit.prevent="getSymptoms" class="flex flex-col gap-4">
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="complaint" class="block text-sm text-left mb-2 font-medium ">Chief Complaint*</label>
              <textarea v-model="complaint" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border focus:border-violet-950 bg-violet-200 rounded-md shadow-sm " placeholder='Main concern or reason for the visit' required />
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="onset" class="block text-sm text-left mb-2 font-medium ">Onset*</label>
              <input v-model="onset" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " :max="today" required />
            </div>
            <div class='w-full'>
              <label for="duration" class="block text-sm text-left mb-2 font-medium ">Duration*</label>
              <select v-model="duration" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="hours">Hours</option>
                <option value="days">Days</option>
                <option value="weeks">Weeks</option>
              </select>
            </div>
            <div class='w-full'>
              <label for="frequency" class="block text-sm text-left mb-2 font-medium ">Frequency*</label>
              <select v-model="frequency" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="constantly">Constant</option>
                <option value="intermittently">Intermittent</option>
                <option value="occasionally">Occosional</option>
              </select>
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="severity" class="block text-sm text-left mb-2 font-medium ">Severity*</label>
              <select v-model="severity" type="date" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " required>
                <option value="mild">Mild</option>
                <option value="moderate">Moderate</option>
                <option value="severe">Severe</option>
              </select>
            </div>
            <div class='w-full'>
              <label for="location" class="block text-sm text-left mb-2 font-medium ">Location*</label>
              <input v-model="location" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="symptom location" required/>
            </div>
            <div class='w-full'>
              <label for="symptomType" class="block text-sm text-left mb-2 font-medium ">Type of Symptom*</label>
              <input v-model="symptomType" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder="pain" required />
            </div>
          </div>
          <div class="flex gap-4">
            <div class='w-full'>
              <label for="otherSymptoms" class="block text-sm text-left mb-2 font-medium ">Other Symptoms</label>
              <textarea v-model="otherSymptoms" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " placeholder='Other Symptoms'/>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button type="button" @click="openModal = true; openPatientSymptoms = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Review of System -->
    <div v-if="openReview" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-full shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Review Of Client </h2>
        <p class="text-center mb-4 text-violet-500"> Note down all reviews patient has </p>
        <form @submit.prevent="getReviewSystem" class="grid grid-cols-2 gap-4">
          <div class="flex flex-col gap-4 p-4">
            <div class='flex flex-row gap-4 '>
              <div class='flex w-full gap-4'>
                <label for="general" class="block text-sm text-left mb-2 font-medium ">General</label>
                <textarea v-model="general" type="text" class="mt-1 ml-20 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revCardiovascular" class="block text-sm text-left mb-2 font-medium ">Cardiovascular</label>
                <textarea v-model="revCardiovascular" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="gastrointestinal" class="block text-sm text-left mb-2 font-medium ">Gastrointestinal</label>
                <textarea v-model="gastrointestinal" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revRespiratory" class="block text-sm text-left mb-2 font-medium ">Respiratory</label>
                <textarea v-model="revRespiratory" type="text" class="mt-1 ml-6 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
          </div>
          <div class="flex flex-col gap-4 p-4">
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="genitourinary" class="block text-sm text-left mb-2 font-medium ">Genitourinary</label>
                <textarea v-model="genitourinary" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="revMusculoskeletal" class="block text-sm text-left mb-2 font-medium ">Musculoskeletal</label>
                <textarea v-model="revMusculoskeletal" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
            <div class='flex flex-row gap-4'>
              <div class='flex w-full gap-4'>
                <label for="revNeurological" class="block text-sm text-left mb-2 font-medium ">Neurological</label>
                <textarea v-model="revNeurological" type="text" class="mt-1 ml-10 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
              <div class='flex w-full gap-4'>
                <label for="psychiatric" class="block text-sm text-left mb-2 font-medium ">Psychiatric</label>
                <textarea v-model="psychiatric" type="text" class="mt-1 ml-8 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
              </div>
            </div>
          </div>
          <div class="col-span-2 flex justify-end gap-4 mt-2">
            <button type="button" @click="navigateBack(); openReview = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Physical Exam -->
    <div v-if="openPhysical" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-full shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-1 text-center"> Physical Exam </h2>
        <p class="text-center text-violet-500 text-sm mb-4"> Check all the test done </p>
        <form @submit.prevent="getPhysicalExam" class="grid grid-cols-2 gap-4 placeholder-violet-950">
          <div class='flex flex-col gap-4'>
            <div>
              <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> Vital Signs </h3>
              <div class="flex flex-col gap-4 rounded-md p-4">
                <div class="flex flex-row gap-4">
                  <div class='flex gap-4'>
                    <input v-model="temperature" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="temperature" required />
                    <input v-model="bloodPressure" type="text" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="blood pressure" required />                  
                    <input v-model="heartRate" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="heart rate" required />
                    <input v-model="respiratoryRate" type="number" class="mt-1 pl-2 block text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950 w-full h-8" placeholder="respiratory rate" required />
                  </div>
                </div>
              </div>
              <div v-if="vitalValidStatus" class="mt-1">
                <p class="text-left text-red-500 pl-2" v-for="(item, index) in vitalErrorMsgs" :key="index">{{ item }}</p>
              </div>
            </div>
            <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> HEENT Examination </h3>
            <div class='flex flex-col gap-4 rounded-md p-4'>
              <div class='flex flex-row gap-4'>
                <div class='flex w-full gap-4'>
                  <textarea v-model="head" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="head" rows='2'/>
                  <textarea v-model="eyes" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="eyes" rows='2'/>
                </div>
              </div>
              <div class='flex flex-row gap-4'>
                <div class='flex w-full gap-4'>
                  <textarea v-model="nose" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="nose" rows='2'/>
                  <textarea v-model="throat" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md placeholder-violet-950" placeholder="throat" rows='2'/>
                </div> 
              </div>
            </div>
          </div>
          <div class='flex flex-col gap-4'>
            <div>
              <h3 class="text-base font-semibold mb-1 text-violet-600 text-center"> Other Examination </h3>
              <div class='flex flex-col gap-4 rounded-md p-4'>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="abdominal" type="text" class="mt-1 placeholder-violet-950 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Abdominal" rows='3'/>
                    <textarea v-model="cardiovascular" type="text" class="mt-1 pl-2 placeholder-violet-950 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Cardiovascular" rows='3'/>
                  </div>
                </div>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="musculoskeletal" type="text" class="mt-1 pl-2 placeholder-violet-950 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Musculoskeletal" rows='3'/>
                    <textarea v-model="neurological" type="text" class="mt-1 pl-2 block placeholder-violet-950 w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Neurological" rows='3'/>
                  </div>
                </div>
                <div class='flex flex-row gap-4'>
                  <div class='flex w-full gap-4'>
                    <textarea v-model="respiratory" type="text" class="mt-1 pl-2 block placeholder-violet-950 w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Respiratory" rows='3'/>
                    <textarea v-model="skin" type="text" class="mt-1 pl-2 block w-full placeholder-violet-950 text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder="Skin" rows='3'/>
                  </div>
                </div>
              </div>
            </div> 
          <div class="flex justify-end gap-4 mt-2">
            <button type="button" @click="openReview = true; openPhysical = false" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </div>
        </form>
      </div>
    </div>

    <!-- Lab Results -->
    <div v-if="openLabResult" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-4 text-center"> Lab Test Results </h2>
        <form @submit.prevent="fillLabResults" class="flex flex-col gap-4">
          <div class="grid grid-cols-2 gap-4 rounded-md p-4">
            <div class="flex flex-col gap-4">
              <div>
                <label for="testName" class="block text-sm text-left mb-2 font-medium ">Test Name</label>
                <input v-model="testName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " placeholder='Enter test conducted' />
              </div>
              <div>
                <label for="testResult" class="block text-sm text-left mb-2 font-medium ">Test Results</label>
                <textarea v-model="testResult" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='3'/>
              </div>
              <div>
                <label for="referenceRange" class="block text-sm text-left mb-2 font-medium ">Reference Range</label>
                <textarea v-model="referenceRange" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='3'/>
              </div>
            </div>
            <div class="flex flex-col gap-4">
              <div>
                <label for="interpretation" class="block text-sm text-left mb-2 font-medium ">Interpretation</label>
                <textarea v-model="interpretation" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md  " rows='4'/>
              </div>
              <div>
                <label for="followup" class="block text-sm text-left mb-2 font-medium ">Follow Up</label>
                <textarea v-model="followup" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " rows='4'/>
              </div>
            </div>
            <div class="flex justify-center gap-4 col-span-2">
              <button @click="addResults" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">Add Another Test</button>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openPhysical = true; openLabResult = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Diagnosis -->
    <div v-if="openDiagnosis" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow text-violet-950">        
        <h2 class="text-xl font-bold mb-4 text-center"> Diagniosis And Treatment Plan </h2>
        <form @submit.prevent="fillTreatmentPlan" class="flex flex-col gap-4">
          <div class="flex flex-row gap-4">
            <label for="diagnosis" class="block text-sm text-left mb-2 font-medium ">Diagniosis*</label>
            <textarea v-model="diagnosis" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " required rows='3'/>
          </div>
          <div class="flex flex-row gap-4">
            <label for="treatment" class="block text-sm text-left mb-2 font-medium ">Treatment Plan*</label>
            <textarea v-model="treatment" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md " required rows='4'/>
          </div>
          <div class="flex flex-row content-center">
            <div class="border border-violet-900 h-0 w-full mt-2"/>
            <h4 class="w-full m-0 text-violet-600 text-center"> Prescribed medicine's </h4>
            <div class="border border-violet-900 h-0 w-full mt-2"/>
          </div>
          <div class="flex flex-row gap-4">
            <div class='w-full'>
              <div class="flex w-full gap-4">
                <div>
                  <label for="medicineName" class="block text-sm text-left mb-2 font-medium ">Medicine Name</label>
                  <input v-model="medicineName" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md "/>
                </div>
                <div class="w-12">
                  <label for="quantity" class="block text-sm text-left mb-2 font-medium ">Qty</label>
                  <input v-model="quantity" type="number" class="mt-1 pl-2 block w-full text-sm py-2 border bg-violet-200 focus:border-violet-950 rounded-md text-dark-blue"/>
                </div>
                <button @click="addMedicine" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md h-[38px] mt-[28px]">add</button>
      
              </div>
              <div v-if="qtyValidStatus" class="mt-4">
                <p class="p-2 text-center rounded text-red-800">
                  Quantity value should be 0 or more
                </p>
              </div>
            </div>
            <div class="w-full">
              <div v-if="added" class='flex flex-col border border-violet-950 rounded-md p-4 h-36 flex-nowrap overflow-auto'>
                <p class="text-form-lb dark: text-left" v-for="(item, index) in medicine" :key="index">{{ item.medicine }}-{{ item.quantity }}</p>
              </div>
            </div>
          </div>
          <div class="flex justify-end gap-4">
            <button @click="openLabResult = true; openDiagnosis = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
            <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md focus:ring focus:ring-btn-fcs">next</button>
          </div>
        </form>
      </div>
    </div>

    <!-- Invoice -->

    <Register />
    <!-- patient data -->
    

    <!-- medical history -->
    <div v-if="openHistory" class="fixed inset-0 z-40 flex justify-center items-center bg-violet-950 bg-opacity-50">
      <div class="bg-violet-300 text-violet-950 rounded-lg shadow-lg p-8 w-full max-w-2xl shadow">        
        <h2 class="text-xl font-bold mb-4 text-center"> Medical History </h2>
        <form @submit.prevent="getHistory" class="grid grid-cols-2 gap-4">
          <div class="flex flex-col gap-4">
            <h4 class="text-center text-violet-600">General Health</h4>
            <div>
              <label for="currentStatus" class="block text-sm text-left mb-2 font-medium ">Current Health</label>
              <textarea v-model="currentStatus" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="allergies" class="block text-sm text-left mb-2 font-medium ">Current Health</label>
              <textarea v-model="allergies" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="medications" class="block text-sm text-left mb-2 font-medium ">Medications</label>
              <textarea v-model="medications" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="surgeries" class="block text-sm text-left mb-2 font-medium ">Surgeries</label>
              <textarea v-model="surgeries" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
            <div>
              <label for="hospitalization" class="block text-sm text-left mb-2 font-medium ">Hospitalizations</label>
              <textarea v-model="hospitalization" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='1'/>
            </div>
          </div>
          <div class="flex flex-col gap-4">
            <h4 class="text-center text-violet-600">Family History</h4>
            <div>
              <label for="parent" class="block text-sm text-left mb-2 font-medium ">Parent's Health Status</label>
              <textarea v-model="parent" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
            </div>
            <div>
              <label for="sibling" class="block text-sm text-left mb-2 font-medium ">Siblings Health Status</label>
              <textarea v-model="sibling" type="text" class="mt-1 pl-2 block w-full text-sm py-2 border  bg-violet-200 focus:border-violet-950 rounded-md shadow-sm " rows='3'/>
            </div>
          </div> 
          <div class="flex justify-end gap-4 h-10">
              <button @click="openModal = true; openPatientInfo = false" type="button" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">back</button>
          </div>
          <div class="flex justify-start gap-4 h-10">
              <button type="submit" class="bg-violet-800 hover:bg-violet-950 text-white font-bold py-2 px-4 rounded-md">next</button>
          </div> 
        </form>
      </div>
    </div>
</template>

<script setup>
    import { UserIcon } from '@heroicons/vue/20/solid';
    import { ref } from 'vue';
    import { useAuthStore } from '@/stores/auth';
    import { usePatientModalStore } from '@/stores/patientModal';
    import Register from '@/components/patients/Register.vue';

    const openModal = ref(false);
    const authStore = useAuthStore();
    const modalStore = usePatientModalStore();

    const alert = ref({ visible: false, message: '' });
    function showAlert(message) {
        alert.value = { visible: true, message };
        setTimeout(() => {
          alert.value.visible = false;
        }, 3000); 
    }

    // Look up modal
    const first = ref("");
    const second = ref("");
    const last = ref("");
    const mobile = ref("");
    const reason = ref("");

    async function LookUpPatient() {
        if (first.value && mobile.value && reason.value) {

            // check if user is already registered
            try {
                const response = await fetch("http://127.0.0.1:8000/patient/check-patient", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        'Authorization': `Bearer ${authStore.getAccessToken}`,
                    },
                    body: JSON.stringify({
                        "mobile": mobile.value,
                        "reason": reason.value,
                        "first": first.value,
                        "second": second.value,
                        "last": last.value,
                    }),
                });

                if (!response.ok) {
                    const errorData = await response.json();
                    showAlert(errorData.error);
                }

                const success = await response.json();
                if (success.registered) {
                    if (reason.value === "emergency") {
                        modalStore.emergencyModal();
                        openModal.value = false;
                    } else if (reason.value === "scheduled care") {
                        modalStore.scheduledModal();
                        openModal.value = false;
                    } else if (reason.value === "disease management") {
                        modalStore.managementModal();
                        openModal.value = false;
                    } else if (reason.value === "maternity care") {
                        modalStore.maternityModal();
                        openModal.value = false;
                    } else if (reason.value === "rehabilitation") {
                        modalStore.rehabilitationModal();
                        openModal.value = false;
                    } else if (reason.value === "palliative care") {
                        modalStore.palliativeModal();
                        openModal.value = false;
                    } else if (reason.value === "consultation") {
                        modalStore.consultationModal();
                        openModal.value = false;
                    } else {
                        showAlert("Invalid reason provided. Please try again")
                        openModal.value = false;
                    }
                } else {
                    modalStore.registerModal();
                    openModal.value = false;
                }
            } catch (error) {
                console.error(error);
                throw error; 
            }   
        }
    }

</script>

  <style>
  .disabled {
    background-color: #6c757d;
    cursor: not-allowed;
  }
</style>