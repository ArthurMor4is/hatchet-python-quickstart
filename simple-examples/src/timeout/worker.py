from ..hatchet import hatchet


@hatchet.workflow(on_events=["timeout:create"])
class TimeoutWorkflow:

    @hatchet.step(timeout='4s')
    def timeout(self, context):
        try:
            print("started step2")
            context.sleep(5)
            print("finished step2")
        except Exception as e:
            print("caught an exception: " + str(e))
            raise e